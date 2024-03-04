def del_brace(str):
    for i in range(len(str)):
        if(str[i] == '['):
            return str[:i-1]
    return str
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ssanmy.settings")
import django
django.setup()

from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup
from ssanmyApp.models import testPost


from apscheduler.schedulers.background import BackgroundScheduler
scheduler = BackgroundScheduler()

def find_obj():
    url = "https://www.fmkorea.com/index.php?mid=hotdeal&category=1254381811&page=1"
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    title = soup.find_all('a', attrs={"class": "hotdeal_var8"})
    data = []
    for i in title:
        data.append(del_brace(i.get_text().strip()))
    return data

@scheduler.scheduled_job('cron', second='*/10')
def start_crawl():
    print('crawling data...')
    obj = find_obj()
    for i in obj:
        testPost(test_title = i).save()

scheduler.start()

if __name__=='__main__':
    start_crawl()
