# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:conftest.py
@Time:2020/11/20 上午9:04
"""
import os
import pytest
from commom.RequestPost import Post
from commom.GetToken import ReturnToken
from commom.GetYaml import GetData


@pytest.fixture(scope='function', autouse=True)
def get_fans_token(get_config):
    # todo: 1.修改读取数据方法； 2.增加写入数据方法
    header = ''
    url1 = 'http://test.api.pokekara.com/api/user/login'
    path = os.path.split(__file__)[0]
    data_path = os.path.join(path, 'test_get_fans')
    # 根据主conftest中的getconfig读取环境配置信息
    if get_config[1] == 'debug':
        data = GetData(path=data_path, envi='debug').get_data()
        print(data)
        a = ReturnToken(url=url1, data=data, header=header).post_request()
        return a
    elif get_config[1] == 'debug':
        data = GetData(path=data_path, envi='online').get_data()
        print(data)
        a = ReturnToken(url=url1, data=data, header=header).post_request()
        return a


def test_one(get_fans_token):
    a = get_fans_token
    print(a)
    assert 1 == 1
