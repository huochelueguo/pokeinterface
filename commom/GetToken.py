# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:GetToken.py
@Time:2020/11/15 下午10:44
"""
# 封装获取token，返回token

from commom.RequestPost import Post

from commom.Logs import Log

# 调用日志模块
log = Log(__name__)
logger = log.Logger


class ReturnToken(Post):

    def __init__(self, url, body, header):
        # 调用父类构造方法
        super().__init__(url, body, header)

    # 重写父类的post_request方法，仅返回token即可
    def post_request(self):
        res = super().post_request()
        res_dict = res[0]
        res_token = res_dict.get('data').get('poke_session_id')
        logger.info('获取token')
        # print(type(res_dict))
        return res_token


if __name__ == '__main__':
    header = ''
    datas = {'platform': 4,
                'token': 'login',
                'id_token': '+8618515588536',
                'secret': '111111'}
    url1 = 'http://test.api.pokekara.com/api/user/login'
    url2 = ''
    datas2 = ''
    a = ReturnToken(url=url1, body=datas, header=header).post_request()
    print(a)
