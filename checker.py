import requests
import threading
import time
from os import system

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
        self.line_split = nice
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


def result():
    print(f"\033[91m\n\nResult:\033[0m\n\n\n"
          f"\033[35mChecked\t : \t{total_checked}\n"
          f"\033[35mValid\t : \t{valid}\n"
          f"\033[35mInvalids\t : \t{invalid}\n")


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
        result()

    except KeyboardInterrupt:
        print('\n\n\033[91mExiting...')
        result()
