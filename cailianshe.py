# coding: utf-8
from __future__ import unicode_literals

from db.models import DBSession, News

import requests
import time
import logging

from filter import filter_by_keywords


def get_lastest_news():
    cursor = 0
    url = 'http://www.cailianpress.com/v2/article/get_roll?type=-1&staid={0}&count=20&flow=1&_={1}'
    url = url.format(cursor, unicode(time.time()).split('.'))
    try:
        resp = requests.get(url, timeout=3)
        data = resp.json()
        next_cursor =
        news_data = data.get('data')
        for itm in data
            title = itm.get('content', '')
            if filter_by_keywords(title):
                news = News()
                news.link = 'http://www.cailianpress.com/'
                news.title = title
                news.sid = itm.get('')
    except Exception as e:
        logging.exception('ERROR in get news from cailianshe cursor {0} reason {1}'.format(e, cursor))

