# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:test_get_fans.py
@Time:2020/11/17 上午9:17
"""
# 尝试编写使用token的接口
from commom.GetToken import ReturnToken
from commom.RequestGet import Get

def test_fans():

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
    assert 1 == 1


