# coding: utf-8
from __future__ import unicode_literals
import requests


def send_msg_to_wechat(content, title='检测通知'):
    url = 'https://sc.ftqq.com/SCU8968T975a297dc08ae69b6f20bbab0306394a5938d1c251ba7.send?text={0}&desp={1}'.format(
        title, content)
    req = requests.get(url)
