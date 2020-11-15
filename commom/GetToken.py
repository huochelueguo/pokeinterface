# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:GetToken.py
@Time:2020/11/15 下午10:44
"""
# 封装获取token，返回token

import requests

from commom.RequestPost import Post


class ReturnToken(Post):

    def __init__(self, url, header, body):
        super().__init__(url, body, header)


    # 重写父类的post_request方法，仅返回token即可
    def get_token(self):
        res = requests.post(url=self.url)
