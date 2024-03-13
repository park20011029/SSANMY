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

        str2 = del_brace_quasar(str2)
    return str2

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ssanmy.settings")
#import django
#django.setup()

from urllib.parse import urlparse

import json
import requests
import time
from bs4 import BeautifulSoup
import datetime

from ssanmyApp.models import Post
from ssanmyApp.models import Postcategory
from ssanmyApp.models import Category
from apscheduler.schedulers.background import BackgroundScheduler

def set_to_arr(title):
    title_arr = []
    for i in title:
        title_arr.append(is_unicord(i.get_text().strip()))
    return title_arr

def find_main(url, attrs):
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    section = soup.find_all('span', attrs)
    data = []
    for i in section:
        data.append(is_unicord(i.get_text().strip()))
    return data

def find_by_parser(response, parser, retry_sec = 2):
    time.sleep(retry_sec)
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }

        soup = BeautifulSoup(response.text, 'html.parser')

        selected = soup.select_one(parser)

        for son in selected.contents:
            if son.get_text() != son:
                son.replaceWith("")

    except AttributeError as err:
        if (retry_sec > 2):
            return None
        else:
            print("access denied retrying in " + str(retry_sec) + "seconds")

            find_by_parser(response, parser, retry_sec * 2)

    else:
        return selected.get_text().strip()

def link_hrefs(main_url, parsers, retry_sec = 2):
    time.sleep(retry_sec)
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
        }

        response = requests.get(main_url)

        soup = BeautifulSoup(response.text, 'html.parser')

        container = parsers.get('container')
        connector = parsers.get('connector')
        head_str_split = main_url.split('/')
        head_str = head_str_split[0] + "//" + head_str_split[2]

        data = []
        data_cnt = 0

        cont = soup.find(attrs=container)

        #print(find_str)
        for href in cont.find_all(attrs=connector):
            tail_str = href.attrs['href']
            data.append(head_str + tail_str)
            data_cnt = data_cnt + 1

        print("caught " + str(len(data)) + " links")

    except AttributeError as err:
        if(retry_sec > 4):
            return None
        else:
            print("access denied retrying in " + str(retry_sec) + "seconds")
            link_hrefs(main_url, parsers, retry_sec * 2)

    else:
        return data

def find_attrs(url, attrs):

    data = []

    response = requests.get(url)

    for key, value in attrs.items():
        attrs_popped = find_by_parser(response, value)
        if attrs_popped is None:
            return None
        data.append(attrs_popped)

    return data



def job():
    lib = get_lib()


    for dict in lib:
        print('crawling data from ' + dict.get('name'))
        main_url = dict.get('url')
        attrs = dict.get('attrs')
        parsers = dict.get('parsers')
        date_encoded = dict.get('date_encoded')

        for url in link_hrefs(main_url, parsers):
            if url is not None:
                data = find_attrs(url, attrs)
                if data is not None:
                    new_date = datetime.datetime.strptime(data[2], date_encoded)
                    data[2] = str(new_date.strftime('%Y-%m-%d %H:%M'))
                    save_db(data)

    #obj2 = find_quasar(dict)
    #for j in obj2:
    #    Post(cate = j).save()

def save_db(data):
    print("crawled :" + data[0])
    #print(data[1])
    #print(data[2])
    Post(post_title=data[0], post_url=data[1], post_created=data[2]).save()


def get_lib():
    obj_lib = []
    path = 'ssanmyApp/crawl_config'
    for filename in os.listdir(path):
        with open(os.path.join(path,filename), 'r') as f:
            obj_lib.append(json.load(f))

    return obj_lib


def start_crawl():
    scheduler = BackgroundScheduler()
    scheduler.add_job(job, 'interval', minutes=30, id='start_crawl', next_run_time=(datetime.datetime.now() + datetime.timedelta(seconds=10)))
    scheduler.start()