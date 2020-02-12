#!/usr/bin/python
# encoding=utf-8

"""
@author: shenke
"""

from crawler import WeatherCrawler


# 保存email内容
def saveEmail(message):
    with open(email_path, 'w', encoding="utf-8") as email:
        email.writelines(message)


if __name__ == "__main__":
    email_path = 'email.html'

    city = 'shandong/jiaozhou'
    weather = WeatherCrawler.WeatherCrawler(city)
    res = weather.weather_content()
    saveEmail(res)
