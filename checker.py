import requests
import threading
import time
from os import system

system('clear')
client_thread = int(input("Threads: "))
path = str(input('Path To Proxy File To Check: '))
system('clear')


def get_list_proxy():
    url = "https://api.proxyscrape.com/?request=getproxies&" \
          "proxytype=http&timeout=10000&country=all&ssl=all&anonymity=all"
    r = requests.get(url)

    return r.text, r.status_code


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

        self.total = 0
        self.valid = 0
        self.invalid = 0

        self.run()

    def run(self):
        if self.text:
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

                        f = open('proxies.txt', 'a')
                        f.write(f"\n{x}")
                        f.close()

                        self.valid += 1

                    except requests.exceptions.ConnectTimeout:
                        print(f'\033[91m[{x}]\t ~> \tConnect timeout!')
                        self.invalid += 1
                        continue
                    except requests.exceptions.ConnectionError:
                        print(f'\033[91m[{x}]\t ~> \tConnection error!')
                        self.invalid += 1
                        continue
                    except requests.exceptions.HTTPError:
                        print(f'\033[91m[{x}]\t ~> \tHTTP error!')
                        self.invalid += 1
                        continue
                    except requests.exceptions.Timeout:
                        print(f'\033[91m[{x}]\t ~> \tTimeout error!')
                        self.invalid += 1
                        continue
                    except requests.exceptions.TooManyRedirects:
                        print(f'\033[91m[{x}]\t ~> \tToo many redirects!')
                        self.invalid += 1
                        continue
                    except Exception as e:
                        print(f'\033[91m[{x}]\t ~> \tUnknown error!\n{e}')
                        self.invalid += 1
                        continue
                else:
                    print('No Proxy')


if __name__ == '__main__':

    global nice
    nice = open_file()

    threads = []
    for z in range(client_thread):
        threads.append(MainApp())
    for thread in threads:
        thread.daemon = True
        thread.start()

while True:
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        print(f"\033[0m\nExiting...\n\n\n")
        exit(0)
