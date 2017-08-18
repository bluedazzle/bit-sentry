# coding: utf-8
from __future__ import unicode_literals

import logging
import datetime
import pytz

from bter import *
from notify import send_msg_to_wechat


def check_eth_eos():
    a = get_current_eos_price()
    b = get_current_eth_price()
    c, t = get_first_eth_eos_ask()
    d = 0.96 * a - b * c
    now = datetime.datetime.now(tz=pytz.timezone('Asia/Shanghai'))
    if d <= 0:
        msg = '[{0:%Y-%m-%d %H:%M:%S}] Detection price difference ${1}'.format(now, d)
        print msg
        return False, msg
    msg = '[{0:%Y-%m-%d %H:%M:%S}] Detection price difference ￥{1} \n eth: ￥{2} eos: ￥{3} \n buy eth/eos lastest ask no {4} x {5}，Expected to profit ${6}'.format(
        now, d, b, a, c, t, d * t)
    print msg
    send_msg_to_wechat(msg)
    return True, msg