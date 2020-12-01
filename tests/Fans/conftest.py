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
DATA_PATH_ZERO = os.path.join(PATH, 'test_get_fans_zero')
DEBUG_DATA_ZERO = GetData(path=DATA_PATH_ZERO, envi='debug').get_data()
ONLINE_DATA_ZERO = GetData(path=DATA_PATH_ZERO, envi='online').get_data()


@pytest.fixture(scope='class', autouse=True)
def get_fans_token(get_config):
    # 根据主conftest中的getconfig读取环境配置信息
    if get_config[1] == 'debug':
        login_data = DEBUG_DATA[1][0][1]  # 读取数据中切割出登录所使用的数据
        token = ReturnToken(url=login_data.get('path'), json=login_data.get('body'),
                            header=login_data.get('headers')).post_request()    # 使用数据登录返回token和uid
    elif get_config[1] == 'online':
        login_data = ONLINE_DATA[1][0][1]  # 读取数据中切割出登录所使用的数据
        token = ReturnToken(url=login_data.get('path'), json=login_data.get('body'),
                            header=login_data.get('headers')).post_request()
    yield token


@pytest.fixture(scope='class', autouse=True)
def get_fans_zero(get_config):
    # 根据主conftest中的getconfig读取环境配置信息
    if get_config[1] == 'debug':
        login_data = DEBUG_DATA_ZERO[1][0][1]  # 读取数据中切割出登录所使用的数据
        token = ReturnToken(url=login_data.get('path'), data=login_data.get('body'),
                            header=login_data.get('headers')).post_request()  # 使用数据登录返回token和uid
    elif get_config[1] == 'online':
        login_data = ONLINE_DATA_ZERO[1][0][1]  # 读取数据中切割出登录所使用的数据
        token = ReturnToken(url=login_data.get('path'), data=login_data.get('body'),
                            header=login_data.get('headers')).post_request()
    yield token


def pytest_generate_tests(metafunc):
    # todo:目前取值为写死的，无法进行参数化，如果多组测试数据，token和对应组怎么插入
    if 'get_fans' in metafunc.fixturenames:
        if metafunc.config.getoption('--envi') == 'debug':
            test_data_ids = DEBUG_DATA[0][1].split()
            test_data = DEBUG_DATA[1][1::]
            metafunc.parametrize('get_fans', test_data, ids=test_data_ids)
        elif metafunc.config.getoption('--envi') == 'online':
            test_data_ids = ONLINE_DATA[0][1].split()
            test_data = ONLINE_DATA[1][1::]
            metafunc.parametrize('get_fans', test_data, ids=test_data_ids)
    if 'get_fans_zero' in metafunc.fixturenames:
        pass



def test_one(get_fans_token):
    a = get_fans_token
    # print(get_fans.get('path'))
    print(a)
    assert 1 == 1
