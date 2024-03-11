def del_brace(str):
    for i in range(len(str)):
        if(str[i] == '['):
            return str[:i-1]
    return str

def del_brace_quasar(str):
    is_brac = 0
    str2 = ""
    for i in range(len(str)):
        if(str[i] == ']'):
            is_brac = 1
            continue
        if(is_brac == 1):
            str2 += str[i]
    if(is_brac == 0):
        return str
    return str2


def is_unicord(str):
    str2 = ""
    for i in range(len(str)):
        if ord(str[i]) >= 0 and ord(str[i]) <= 65535:
            str2 += str[i]

    return str2

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ssanmy.settings")
#import django
#django.setup()

from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup

from ssanmyApp.models import testPost
from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()

def find_fmkor():
    url = "https://www.fmkorea.com/index.php?mid=hotdeal&category=1254381811&page=1"
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    title = soup.find_all('a', attrs={"class": "hotdeal_var8"})
    data = []
    for i in title:
        data.append(del_brace(i.get_text().strip()))
    return data

def find_quasar():
    url = "https://quasarzone.com/bbs/qb_saleinfo?_method=post&type=&page=1&_token=qqltYTHszsDxg2JFwC1vLKVL55G4fYaPDdKdLsMD&category=PC%2F%ED%95%98%EB%93%9C%EC%9B%A8%EC%96%B4&popularity=&kind=subject&keyword=&sort=num%2C+reply&direction=DESC"
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    title = soup.find_all('span', attrs={"class": "ellipsis-with-reply-cnt"})
    data = []
    for i in title:
        data.append(del_brace_quasar(is_unicord(i.get_text().strip())))
    return data

def find_coolenjoy():
    url = "https://coolenjoy.net/bbs/jirum?sca=PC%EA%B4%80%EB%A0%A8"
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    title = soup.find_all('a', attrs={"class": "na-subject"})
    data = []
    for i in title:
        data.append(del_brace_quasar(is_unicord(i.get_text().strip())))
    return data

def job():
    print('crawling data from fmkorea...')
    obj = find_fmkor()
    for i in obj:
        testPost(test_title = i).save()
    print('crawling data from quasar...')
    obj2 = find_quasar()
    for j in obj2:
        testPost(test_title = j).save()
    print('crawling data from coolenjoy...')
    obj3 = find_coolenjoy()
    for k in obj3:
        testPost(test_title=k).save()

def start_crawl():
    scheduler = BackgroundScheduler()
    scheduler.add_job(job, 'interval', seconds=10, id='start_crawl')
    scheduler.start()