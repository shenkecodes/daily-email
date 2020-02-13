#!/usr/bin/python
# encoding=utf-8

"""
@author: shenke
"""

import requests
from bs4 import BeautifulSoup


class OneArticle:
    """
    爬取One文章
    """

    # 爬取内容
    def __get_article(self):
        url = 'http://wufazhuce.com/'

        response = requests.get(url)
        if (response.status_code == 200):
            soup = BeautifulSoup(response.text, "html.parser")

            img = soup.find('img', attrs={'class': 'fp-one-imagen'}).get('src')
            title = soup.find('div', attrs={'class': 'fp-one-cita'}).find('a').string

            return img, title

        else:
            return None

    # 渲染成html
    def article_content(self):

        try:
            img, title = self.__get_article()
            article_html = '<div style="margin: 20px 0;width:100%;text-align:center"><div><em style="color:#424242">—————— ONE ——————</em></div>' + \
                           '<img style="margin: 20px 0;width:80%;border-radius:5px;" src="' + img + '" /><div style="margin: 20px 0;"><em>' + title + '</em></div></div>'

            return article_html

        except Exception as e:
            print('Error: ' + str(e))
            return ''
