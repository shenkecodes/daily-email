#!/usr/bin/python
# encoding=utf-8

"""
@author: shenke
"""

import requests


class LoveWords:
    """
    土味情话，使用天行API
    """

    def __init__(self, APIKEY):
        self.__APIKEY = APIKEY

    def __get_words(self):
        url = 'http://api.tianapi.com/txapi/saylove/index?key=' + self.__APIKEY
        response = requests.get(url)
        if (response.status_code == 200):
            res = response.json()
            content = res['newslist'][0]['content'].strip()

            return content
        else:
            return None

    def words_content(self):

        try:
            res = self.__get_words()
            words_html = '<div style="margin: 20px 0;width:100%;text-align:center"><em style="color:#424242">—————— 情话 ——————</em></div>' + \
                         '<p style="width:100%;text-align:center;color:darkslateblue;">' + res + '</p>'

            return words_html

        except Exception as e:
            print('Error: ' + str(e))
            return ''
