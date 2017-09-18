# coding: utf-8
from __future__ import unicode_literals

from datetime import datetime

from db.models import DBSession, News
from cache.cache import redis_1

import requests
import time
import logging

from filter import filter_by_keywords
from notify import send_msg_to_wechat
from utils import md5


def get_lastest_news(the_cursor):
    session = DBSession()
    cursor = redis_1.get("cls_cursor")
    if not cursor:
        latest = session.query(News).filter(News.source == 1).order_by(News.create_time.desc()).first()
        if not latest:
            cursor = the_cursor
        else:
            cursor = latest.sid
    url = 'http://www.cailianpress.com/v2/article/get_roll?type=-1&staid={0}&count=20&flow=1&_={1}'
    url = url.format(cursor, unicode(time.time()).split('.')[0])
    try:
        resp = requests.get(url, timeout=3)
        data = resp.json()
        no_new = data.get('errno', None)
        if no_new == 20022:
            return False
        news_data = data.get('data')
        next_cursor = news_data[0].get('sort_score')
        redis_1.set('cls_cursor', next_cursor)
        for itm in news_data:
            title = itm.get('content', '')
            if filter_by_keywords(title):
                news = News()
                news.link = 'http://www.cailianpress.com/'
                news.title = title
                news.source = 1
                news.sid = next_cursor
                news.hash = md5(title.encode('utf-8'))
                session.add(news)
                send_msg_to_wechat(title, '资讯 {0:%Y-%m-%d %H:%M:%S}'.format(datetime.now()))
        try:
            session.commit()
            session.close()
        except Exception as e:
            logging.exception('ERROR in commit data to database reason {0}'.format(e))
            session.rollback()
    except Exception as e:
        logging.exception('ERROR in get news from cailianshe cursor {0} reason {1}'.format(e, cursor))
        return False