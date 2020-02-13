#!/usr/bin/python
# encoding=utf-8

"""
@author: shenke
"""

import requests
from bs4 import BeautifulSoup


class WeiboRank:
    """
    爬取新浪微博热搜
    """

    # 爬取内容
    def __get_rank(self):
        url_prefix = 'https://s.weibo.com'

        url = url_prefix + '/top/summary'

        response = requests.get(url)
        if (response.status_code == 200):
            soup = BeautifulSoup(response.text, "html.parser")

            rank_list = []
            rank_source = soup.find_all('td', attrs={'class': 'td-02'})

            for i in rank_source:
                title = i.find('a').string
                link = url_prefix + i.find('a').get('href')
                rank_list.append([title, link])

            rank_list.pop(0)
            return rank_list
        else:
            return None

    # 渲染成html
    def rank_content(self):

        try:
            rank_html = '<div style="display: flex;flex-direction: column;align-items: center;margin: auto;">' + \
                        '<div style="margin: 20px 0;width:100%;text-align:center;margin-bottom:5px;"><em style="color:#424242">—————— <img src="https://imgs.t.sinajs.cn/t6/style/images/global_nav/WB_logo.png?id=1404211047727" /> ——————</em></div>'
            rank_list = self.__get_rank()
            length = 10

            for index in range(length):
                rank_html += '<a style="margin:7px;padding:8px 5px;color:black;text-decoration:none"href="' + \
                             rank_list[index][1] + '"><b style="color: #f26d5f;">' + str(index + 1) + '</b> ' + \
                             rank_list[index][0] + '</a>'

            rank_html += '</div>'
            return rank_html
        except Exception as e:
            print('Error: ' + str(e))
            return ''
