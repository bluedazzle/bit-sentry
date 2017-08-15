# coding: utf-8
from __future__ import unicode_literals
import requests
import json

from tornado.httpclient import AsyncHTTPClient

ETH_CNY_URL = 'http://data.bter.com/api2/1/ticker/eth_cny'
EOS_CNY_URL = 'http://data.bter.com/api2/1/ticker/eos_cny'
ETH_EOS_URL = 'http://data.bter.com/api2/1/ticker/eos_eth'
ETH_EOS_ORDER_URL = 'http://data.bter.com/api2/1/orderBook/eos_eth'


def get_current_eth_price():
    # client = AsyncHTTPClient()
    req = requests.get(ETH_CNY_URL, timeout=5)
    # rsp = client.fetch(ETH_CNY_URL)
    # print rsp.result()
    rsp = req.content
    data = json.loads(rsp)
    if data.get('result') == 'true':
        return data.get('last')


def get_current_eos_price():
    req = requests.get(EOS_CNY_URL, timeout=5)
    rsp = req.content
    data = json.loads(rsp)
    if data.get('result') == 'true':
        return data.get('last')


def get_first_eth_eos_ask():
    req = requests.get(ETH_EOS_ORDER_URL, timeout=5)
    rsp = req.content
    data = json.loads(rsp)
    if data.get('result') == 'true':
        asks = data.get('asks')
        ask = asks[-1]
        # price, count
        return ask[0], ask[1]


        # e = (c - 0.02) * b - a