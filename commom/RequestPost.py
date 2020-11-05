# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:RequestPost.py
@Time:2020/8/19 上午9:06
"""
# post请求的封装,返回相应内容和响应码

import requests


class Post(object):

    """
    封装post方法
    """

    def __init__(self, url, body, header):
        self.url = url
        self.body = body
        self.header = header

    def post_request(self):
        try:
            if self.url == '':
                print('输入地址为空，请检查')
            elif self.body == '':
                print('输入请求体为空，请检查')
            elif self.header == '':
                response = requests.post(url=self.url, data=self.body)
                return response.json(), response.status_code
            else:
                response = requests.post(url=self.url, data=self.body, headers=self.header)
                return response.json(), response.status_code
        except Exception as result:
            print(result)


if __name__ == '__main__':
    header = ''
    datas = {'platform': 4,
                'token': 'login',
                'id_token': '+8618515588536',
                'secret': '111111'}
    url1 = 'http://test.api.pokekara.com/api/user/login'
    url2 = ''
    datas2 = ''
    a = Post(url1, datas, header).post_request()
    print(a[1])
