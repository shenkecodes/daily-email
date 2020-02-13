#!/usr/bin/python
# encoding=utf-8

"""
@author: shenke
"""

import json
from crawler import weather, weibo_rank, love_words, one_article, countdown


# 保存email内容
def saveEmail(message):
    with open(email_path, 'w', encoding="utf-8") as email:
        email.writelines(message)


if __name__ == "__main__":
    email_path = 'email.html'
    config_path = 'config.json'

    with open(config_path, 'r', encoding='utf-8') as f:
        config = json.load(f)

    APIKEY = config['APIKEY']
    important_day = config['important_day']
    cities = config['cities']

    # 生日倒计时
    bir_countdown_html = countdown.Countdown(APIKEY, important_day).bir_countdown_content()
    # 天气卡片
    weather_html = weather.WeatherCrawler(cities).weather_content()
    # 土味情话
    words_html = love_words.LoveWords(APIKEY).words_content()
    # One文章
    article_html = one_article.OneArticle().article_content()
    # 微博热搜前十
    rank_html = weibo_rank.WeiboRank().rank_content()

    html = bir_countdown_html + weather_html + words_html + article_html + rank_html
    saveEmail(html)
