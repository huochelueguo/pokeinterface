# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:GetToken.py
@Time:2020/11/15 下午10:44
"""
# 封装获取token，返回token
import json
from commom.RequestPost import Post
from commom.Logs import Log

# 调用日志模块
log = Log(__name__)
logger = log.Logger


class ReturnToken(Post):

    def __init__(self, url, header, data=None, json=None):
        """调用父类构造方法"""
        super().__init__(url, header, data, json)
        self.url = url
        self.header = header
        self.data = data
        self.json = json

    def post_request(self, kwargs=None):
        """重写父类的post_request方法，仅返回token即可"""
        try:
            res = super().post_request()
            res_dict = res[0]
            res_token = res_dict.get('data').get('poke_session_id')
            res_uid = res_dict.get('data').get('user').get('uid')
            str1 = 'poke_session_id='
            token = str1 + res_token
        except Exception as result:
            print(result)
            logger.error(f'获取token出错：{result}')
        # print(res_uid)
        else:
            logger.info('获取到token和uid返回')
            return token, res_uid


if __name__ == '__main__':
    header = {'Content-Type': 'application/json'}
    datas = {'platform': 4,
                'token': 'login',
                'id_token': '+8618515588536',
                'secret': '111111'}
    # header = {'Content-Type': 'application/x-www-form-urlencoded'}
    # datas = {'platform': 7,
    #             'token': 'login',
    #             'id_token': 'pk1606824368991752854',
    #             'secret': '$2a$10$Psy5oL27FW.scEt3gPABtOLSv2GnHH8XxCyj53v7KMj/lObQDWNZe'}
    url1 = 'https://test.api.pokekara.com/api/user/login'
    url2 = ''
    datas2 = ''
    a = ReturnToken(url=url1, json=datas, header=header).post_request()
    print(a)
