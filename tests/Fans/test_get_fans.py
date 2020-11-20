# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:test_get_fans.py
@Time:2020/11/17 上午9:17
"""
# 尝试编写使用token的接口，整体流程：
# 1.conftest中创建一个fixture,该fixture先通过主fixture获取环境配置，根据环境配置读取数据
# 2.对数据进行拆分，抓取出登录需要的数据，调用gettoken方法，获取到token
# 3.再使用pytest.generate.tests对case进行参数化
import os

from commom.GetToken import ReturnToken
from commom.RequestGet import Get
from commom.GetYaml import GetData
def test_fans():

    header = ''
    datas = {'platform': 4,
                'token': 'login',
                'id_token': '+8618515588536',
                'secret': '111111'}
    url1 = 'http://test.api.pokekara.com/api/user/login'
    a = ReturnToken(url=url1, data=datas, header=header).post_request()
    print(a)

    url2 = 'http://test.api/user/relationship/followers'
    path = os.path.abspath(__file__)
    s = GetData(path=path, envi='debug').get_data()
    print(s)



