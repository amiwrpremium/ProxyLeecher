import threading
from os import system

import requests
from prettytable import PrettyTable
from termcolor import colored

system('clear')
client_thread = int(input("Threads: "))

if client_thread <= 0:
    print("Are you shitting me?")
    exit(0)

path = str(input('Path To Proxy File To Check: '))
if '.txt' not in path:
    path = f'{path}.txt'
system('clear')


def open_file():
    try:
        with open(path, 'r') as f:
            text = f.read()

        line_split = text.split('\n')
        total = len(line_split)

        print(f'\033[94mLoaded "{total}" proxies\033[39m')
        print(f'\033[94mThread has been set to: "{client_thread}" \n\n\033[39m')
        return line_split

    except FileNotFoundError:
        print(colored(f"Error!\n{path} Not Found\n\nExiting", 'red'))
        exit(0)


total_checked = 0
valid = 0
invalid = 0


def check(current):
    global total_checked
    global valid
    global invalid

    x = current.replace("\r", "")

    if x:
        print(f'\n\033[0m[{x}]\t ~> \tProxy checking...\033[39m', end='')

        try:
            requests.get("http://ipinfo.io/json", proxies={'http': 'http://' + x}, timeout=5)

            print(f'\n\033[92m[{x}]\t ~> \tProxy valid!\033[39m', end='')

            f = open('good.txt', 'a')
            f.write(f"\n{x}")
            f.close()

            valid += 1
            total_checked += 1

        except requests.exceptions.ConnectTimeout:
            print(f'\n\033[91m[{x}]\t ~> \tConnect timeout!\033[39m', end='')
            invalid += 1
            total_checked += 1
            pass
        except requests.exceptions.ConnectionError:
            print(f'\n\033[91m[{x}]\t ~> \tConnection error!\033[39m', end='')
            invalid += 1
            total_checked += 1
            pass
        except requests.exceptions.HTTPError:
            print(f'\n\033[91m[{x}]\t ~> \tHTTP error!\033[39m', end='')
            invalid += 1
            total_checked += 1
            pass
        except requests.exceptions.Timeout:
            print(f'\n\033[91m[{x}]\t ~> \tTimeout error!\033[39m', end='')
            invalid += 1
            total_checked += 1
            pass
        except requests.exceptions.TooManyRedirects:
            print(f'\n\033[91m[{x}]\t ~> \tToo many redirects\033[39m!', end='')
            invalid += 1
            total_checked += 1
            pass
        except Exception as e:
            print(f'\n\033[91m[{x}]\t ~> \tUnknown error!\033[39m\n{e}', end='')
            invalid += 1
            total_checked += 1
            pass
    else:
        print('No Proxy')


class MainApp(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.line_split = nice

    def run(self):
        for i in range(len(self.line_split)):
            try:
                current = self.line_split.pop(i)
            except:
                current = None
                exit(0)

            check(current)


def result():
    table = PrettyTable()
    table.title = colored('Result', 'blue')
    table.field_names = ['Info', 'Count']
    table.add_row([colored('Good', 'green'), colored(str(valid), 'green')])
    table.add_row([colored('Bad', 'red'), colored(str(invalid), 'red')])
    table.add_row([colored('Total', 'cyan'), colored(str(total_checked), 'cyan')])
    try:
        print(table)
    except Exception as e:
        print(colored(f"Error!\n{e}\n\nCouldn't Print Result Table\n", 'red'))


if __name__ == '__main__':
    try:
        global nice
        nice = open_file()

        threads = []
        for z in range(client_thread):
            threads.append(MainApp())
        for thread in threads:
            thread.daemon = True
            thread.start()
        for thread in threads:
            thread.join()

        print('\n\nFinished\nValid proxies saved in good.txt\033[39m\n\n')
        result()

    except KeyboardInterrupt:
        print('\n\n\033[91mExiting...\nValid proxies saved in good.txt\033[39m\n\n')
        result()
