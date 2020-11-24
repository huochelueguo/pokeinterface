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

PATH = os.path.split(__file__)[0]
DATA_PATH = os.path.join(PATH, 'test_get_fans')
DEBUG_DATA = GetData(path=DATA_PATH, envi='debug').get_data()
ONLINE_DATA = GetData(path=DATA_PATH, envi='online').get_data()


@pytest.fixture(scope='class', autouse=True)
def get_fans_token(get_config):
    global DEBUG_DATA
    # todo: scope要改成class
    # 根据主conftest中的getconfig读取环境配置信息
    if get_config[0] == 'debug':
        DEBUG_DATA = GetData(path=DATA_PATH, envi='debug').get_data()
        print(DEBUG_DATA)
    elif get_config[1] == 'online':
        DEBUG_DATA = GetData(path=DATA_PATH, envi='online').get_data()
    login_data = DEBUG_DATA[1][0][1]  # 读取数据中切割出登录所使用的数据
    print(DEBUG_DATA[1][1])
    print(DEBUG_DATA[0][1].split())
    token = ReturnToken(url=login_data.get('path'), json=login_data.get('body'), header=login_data.get('headers')).post_request()
    yield token


def pytest_generate_tests(metafunc):
    if 'get_fans' in metafunc.fixturenames:
        if metafunc.config.getoption('--envi') == 'debug':
            test_data = DEBUG_DATA
            metafunc.parametrize('get_fans', list(test_data[1][1]), ids=test_data[0][1].split())
        elif metafunc.config.getoption('--envi') == 'online':
            test_data = ONLINE_DATA
            metafunc.parametrize('get_fans', list(test_data[1][1]), ids=test_data[0][1].split())


def test_one(get_fans_token,get_fans):
    a = get_fans_token
    print(get_fans)
    print(a)
    assert 1 == 1
