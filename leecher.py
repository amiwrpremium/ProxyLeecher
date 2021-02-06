import requests
from bs4 import BeautifulSoup
from base64 import b64decode
import re
import sys


def free_proxy_list():
    print(f"In : {sys._getframe().f_code.co_name}")
    url = 'https://free-proxy-list.net/'

    user_agent = {
        'user-agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
    }

    r = requests.get(url, headers=user_agent)

    soup = BeautifulSoup(r.content, features="lxml")

    proxies = soup.findAll('textarea')[0].text[75:]

    with open('proxy.txt', 'a+') as f1:
        f1.write(proxies)


def xcoder():
    print(f"In : {sys._getframe().f_code.co_name}")
    r = requests.get('https://xcoder.fun/p.php?r=y')

    with open('proxy.txt', 'a+') as f2:
        f2.write(r.text.replace('\n', ''))


def http_tunnel():
    print(f"In : {sys._getframe().f_code.co_name}")
    url = 'http://www.httptunnel.ge/ProxyListForFree.aspx'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, features="lxml")
    table = soup.find('table', attrs={'id': 'ctl00_ContentPlaceHolder1_GridViewNEW'})
    tr = table.findAll('tr')[1:]
    for x in tr:
        nice = x.find('a').text
        with open('proxy.txt', 'a+') as f3:
            f3.write(f"{nice}\n")


def hide_my_name():
    print(f"In : {sys._getframe().f_code.co_name}")
    for i in range(34):
        url = f'https://hidemy.name/en/proxy-list/?start={i*64}#list/'

        user_agent = {
            'user-agent':
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
        }

        r = requests.get(url, headers=user_agent)
        soup = BeautifulSoup(r.content, features="lxml")
        tbody = soup.find('tbody')
        tr = tbody.findAll('tr')
        for x in tr:
            ip = x.findAll('td')[0].text
            port = x.findAll('td')[1].text

            with open('proxy.txt', 'a+') as f4:
                f4.write(f"{ip}:{port}\n")


def free_proxy():
    print(f"In : {sys._getframe().f_code.co_name}")
    pattern = r'(?<=\(")(.*?)(?="\))'
    for i in range(151):
        url = f'http://free-proxy.cz/en/proxylist/main/{i + 1}'
        r = requests.get(url)
        soup = BeautifulSoup(r.content, features="lxml")
        tbody = soup.findAll('tbody')[0]
        tr = tbody.findAll('tr')
        proxy = ''
        base = r'Base64.decode'
        for x in tr:
            try:
                w = re.findall(base, str(x.find('td')))[0]
            except:
                w = None

            if w:
                ip = b64decode(re.findall(pattern, str(x.findAll('td')[0].find('script')))[0]).decode('utf-8')
                port = x.findAll('td')[1].text
                proxy = f"{proxy}{ip}:{port}\n"

            else:
                pass

        with open('proxy.txt', 'a+') as f5:
            f5.write(f"\n")



def spysme1():
    print(f"In : {sys._getframe().f_code.co_name}")
    url = 'https://spys.me/proxy.txt'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, features="lxml")
    proxies = soup.find('p').text[384:]
    pattern = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5})'

    proxies = re.findall(pattern, proxies)
    proxy = ''
    for ip, port in proxies:
        proxy = f'{proxy}{ip}:{port}\n'

    with open('proxy.txt', 'a+') as f6:
        f6.write(proxy)

