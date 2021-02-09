import requests
import threading
from os import system
from prettytable import PrettyTable
from termcolor import colored

system('clear')
client_thread = int(input("Threads: "))
path = str(input('Path To Proxy File To Check: '))
system('clear')


def open_file():
    with open(path, 'r') as f:
        text = f.read()

    line_split = text.split('\n')
    total = len(line_split)

    print(f"\033[94mLoaded {total} proxies\n\n")

    return line_split


class MainApp(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.tasks = []
        self.text = True
        self.line_split = open_file()
        self.file_path = None

    def run(self):
        if self.text:

            global total_checked
            global valid
            global invalid

            total_checked = 0
            valid = 0
            invalid = 0

            for i in range(len(self.line_split)):
                try:
                    current = self.line_split.pop(i)
                except:
                    current = None
                    exit(0)

                x = current.replace("\r", "")

                if x:
                    print(f'\033[0m[{x}]\t ~> \tProxy checking...')

                    try:
                        requests.get("http://ipinfo.io/json", proxies={'http': 'http://' + x}, timeout=5)

                        print(f'\033[92m[{x}]\t ~> \tProxy valid!')

                        f = open('good.txt', 'a')
                        f.write(f"\n{x}")
                        f.close()

                        valid += 1
                        total_checked += 1

                    except requests.exceptions.ConnectTimeout:
                        print(f'\033[91m[{x}]\t ~> \tConnect timeout!')
                        invalid += 1
                        total_checked += 1
                        continue
                    except requests.exceptions.ConnectionError:
                        print(f'\033[91m[{x}]\t ~> \tConnection error!')
                        invalid += 1
                        total_checked += 1
                        continue
                    except requests.exceptions.HTTPError:
                        print(f'\033[91m[{x}]\t ~> \tHTTP error!')
                        invalid += 1
                        total_checked += 1
                        continue
                    except requests.exceptions.Timeout:
                        print(f'\033[91m[{x}]\t ~> \tTimeout error!')
                        invalid += 1
                        total_checked += 1
                        continue
                    except requests.exceptions.TooManyRedirects:
                        print(f'\033[91m[{x}]\t ~> \tToo many redirects!')
                        invalid += 1
                        total_checked += 1
                        continue
                    except Exception as e:
                        print(f'\033[91m[{x}]\t ~> \tUnknown error!\n{e}')
                        invalid += 1
                        total_checked += 1
                        continue
                else:
                    print('No Proxy')

        print(f"\n\n\n\n\n\t\t  HI  1   \t\t\n\n\n\n\n")


def result():
    table = PrettyTable()
    table.title = colored('Result', 'blue')
    table.field_names = ['Info', 'Count']
    table.add_row([colored('Good', 'green'), colored(str(valid), 'green')])
    table.add_row([colored('Bad', 'red'), colored(str(invalid), 'red')])
    table.add_row([colored('Total', 'cyan'), colored(str(total_checked), 'cyan')])
    print(table)


if __name__ == '__main__':
    try:
        global nice

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
