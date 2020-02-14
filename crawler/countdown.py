#!/usr/bin/python
# encoding=utf-8

"""
@author: shenke
"""

import requests
from datetime import datetime


class Countdown:
    """
    计算生日、纪念日倒计时，使用天行API
    """

    def __init__(self, APIKEY, important_day):
        self.APIKEY = APIKEY
        self.important_day = important_day

    # 返回农历生日的公历日
    def __get_gregoriandate(self, lunardate):
        url = 'http://api.tianapi.com/txapi/lunar/index?key=' + self.APIKEY + '&date=' + lunardate

        response = requests.get(url)
        if (response.status_code == 200):
            res = response.json()
            gregoriandate = res['newslist'][0]['gregoriandate']

            return gregoriandate
        else:
            return None

    # 返回农历生日倒计时
    def __birthday_countdown(self, year):
        date = str(year) + '-' + self.important_day['birthday']
        gregoriandate = datetime.strptime(self.__get_gregoriandate(date), '%Y-%m-%d %H:%M:%S')
        today = datetime.now()
        delta = gregoriandate - today

        if (delta.days < 0):
            return self.__birthday_countdown(year + 1)
        else:
            days = delta.days
            hours = int(delta.seconds / 60 / 60)
            minutes = int((delta.seconds - hours * 60 * 60) / 60)
            seconds = delta.seconds - hours * 60 * 60 - minutes * 60
            return str(gregoriandate), days, hours, minutes, seconds

    # 渲染生日倒计时html
    def bir_countdown_content(self):
        year = datetime.now().year
        gregoriandate, days, hours, minutes, seconds = self.__birthday_countdown(year)
        gregoriandate = gregoriandate.replace(' 00:00:00', '')

        bir_countdown_html = '<p style="">距离你的生日 %s 还有 %s 天 %s 时 %s 分 %s 秒</p>' % (
            gregoriandate, days, hours, minutes, seconds)

        return bir_countdown_html
