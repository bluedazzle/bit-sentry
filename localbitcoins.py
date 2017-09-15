# coding: utf-8
from __future__ import unicode_literals

from lbcapi import api

HMAC_KEY = '25c00b2ac4357030a28507bde0316d8a'
HMAC_SECRET = 'd7f646c6ee45322db5910e46c55c82a427c6aa555d7172f2709b8d8f90a20ef5'

net = api.hmac(HMAC_KEY, HMAC_SECRET)
print net.call('GET', '/sell-bitcoins-online/usd/paypal/.json').json()

