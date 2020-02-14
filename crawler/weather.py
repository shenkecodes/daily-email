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

    def __init__(self, cities):
        self.__cities = cities

    # 爬取内容
    def __get_weather(self, city):
        url = 'https://tianqi.moji.com/weather/china/' + city
        response = requests.get(url)
        if (response.status_code == 200):
            soup = BeautifulSoup(response.text, "html.parser")

            # 背景图片
            background = soup.find('div', id='skin').get('data-url')
            city_name = soup.find('div', attrs={'class': 'search_default'}).find('em').string
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
                'city_name': city_name,
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
            weather_html = '<div style="margin: 20px 0;width:100%;text-align:center;margin-bottom:5px;"><em style="color:#424242">—————— 天气 ——————</em></div>'

            for city in self.__cities:
                res = self.__get_weather(city)

                bg_style = '<div style="margin-bottom:10px;padding:5px;height:200px;text-align:center;color:white;border-radius:5px;background:url(' + \
                           res['background'] + ');background-size:100% 100%;">'
                city_style = '<p style="margin: 10px 0 0 0;font-size: large;">' + res['city_name'] + '</p>'
                body_style = '<div style="width:50%;height:70%;float:left;text-align:left;display:flex;flex-direction:column;justify-content: space-around;">' \
                             '<span>空气质量 &ensp;' + res['air_quality'] + '</span>' + \
                             '<span>湿度 &ensp;' + res['humidity'] + '</span>' + \
                             '<span>风向 &ensp;' + res['wind'] + '</span></div>'

                wea_style = '<div style="width:50%;height:70%;float:right">' + \
                            '<div style="width:100%;font-size:50px;">' + res['temperature'] + '℃</div>' + \
                            '<span style="font-size:20px;"><img style="height:60px;width:60px;" src="' + \
                            res['weather_img'] + '" />&ensp;' + res['weather'] + '</span>' + \
                            '</div><p style="margin: 10px 0 0 0;font-size: large;">' + res['tips'] + '</p></div>'

                content = bg_style + city_style + body_style + wea_style
                weather_html += content

            return weather_html

        except Exception as e:
            print('Error: ' + str(e))
            return ''
