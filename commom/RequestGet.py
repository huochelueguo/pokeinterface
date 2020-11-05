# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:RequestGet.py
@Time:2020/8/21 上午8:56
"""
# 封装get方法

import requests


class Get(object):

    """
    封装get方法
    """

    def __init__(self, url):
        self.url = url

    def get_request(self):
        try:
            if self.url == '':
                print('传入内容为空，请检查')
            else:
                response = requests.get(url=self.url)
                return response.json()
        except Exception as result:
            print(result)


if __name__ == '__main__':
    url1 = 'http://test.api.pokekara.com/x/artist/simple_info?artist_id=512'
    a = Get(url1).get_request()
    print(a)

