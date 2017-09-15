# coding: utf-8
from __future__ import unicode_literals


def filter_by_keywords(content):
    keywords = ['比特', 'btc', 'BTC', 'ETH', 'eth', 'ICO', 'ico', '交易所', '虚拟', '数字']
    for keyword in keywords:
        if keyword in content:
            return True
    return False
