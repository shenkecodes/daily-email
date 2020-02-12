#!/usr/bin/python
# encoding=utf-8

"""
@author: shenke
"""

import requests
from bs4 import BeautifulSoup


class WeatherCrawler:
    """
    爬取天气
    """

    def __init__(self, city):
        self.city = city

    # 爬取内容
    def __get_weather(self):
        url = 'https://tianqi.moji.com/weather/china/' + self.city
        response = requests.get(url)
        if (response.status_code == 200):
            soup = BeautifulSoup(response.text, "html.parser")

            # 背景图片
            background = soup.find('div', id='skin').get('data-url')
            # 空气质量
            air_quality = soup.find('div', attrs={'class': 'wea_alert clearfix'}).find('em').string
            # 今日天气提示
            tips = soup.find('div', attrs={'class': 'wea_tips clearfix'}).find('em').string

            wea_weather = soup.find('div', attrs={'class': 'wea_weather clearfix'})
            # 温度
            temperature = wea_weather.find('em').string
            # 天气
            weather = wea_weather.find('img').get('alt')
            # 天气图标
            weather_img = wea_weather.find('img').get('src')

            wea_about = soup.find('div', attrs={'class': 'wea_about clearfix'})
            # 湿度
            humidity = wea_about.find('span').string
            # 风向
            wind = wea_about.find('em').string

            res = {
                'background': background,
                'air_quality': air_quality,
                'tips': tips,
                'temperature': temperature,
                'weather': weather,
                'weather_img': weather_img,
                'humidity': humidity,
                'wind': wind
            }
            return res
        else:
            return None

    # 渲染html
    def weather_content(self):
        try:
            res = self.__get_weather()

            bg_style = '<div style="padding:5px;height:180px;text-align:center;color:white;border-radius:5px;background:url(' + \
                       res['background'] + ');background-size:100% 100%;">'
            body_style = '<div style="width:50%;height:85%;float:left;text-align:left;display:flex;flex-direction:column;justify-content: space-around;">' \
                         '<span>空气质量 &ensp;' + res['air_quality'] + '</span>' + \
                         '<span>湿度 &ensp;' + res['humidity'] + '</span>' + \
                         '<span>风向 &ensp;' + res['wind'] + '</span></div>'

            wea_style = '<div style="width:50%;height:85%;float:right">' + \
                        '<div style="width:100%;font-size:50px;">' + res['temperature'] + '℃</div>' + \
                        '<span style="font-size:20px;"><img style="height:60px;width:60px;" src="' + \
                        res['weather_img'] + '" />&ensp;' + res['weather'] + '</span>' + \
                        '</div><p>' + res['tips'] + '</p></div>'

            content = bg_style + body_style + wea_style
            return content

        except Exception as e:
            print('Error: ' + str(e))
            return ''
