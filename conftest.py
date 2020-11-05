# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:conftest.py
@Time:2020/8/12 上午9:12
"""
import os

import pytest

from commom.GetYaml import GetData
from config.ReadConfig import ReadConfig


# 获取环境配置
@pytest.fixture(scope='session', autouse=True)
def get_config(request):
    global url
    # envi = 'debug'
    envi = request.config.getoption('--envi')
    try:
        url = ReadConfig().get_envi(env=envi)
    except Exception as result:
        print(result)
    yield url, envi


def pytest_addoption(parser):
    parser.addoption("--envi",
                     action="store",
                     default="debug",
                     help="environment: debug or online")

def test_one(get_config,request):
    # url2 = 'http://test.api.pokekara.com'
    # print(get_config[0])
    # print(get_config)
    # assert get_config[0] == url2
    # if get_config[test_1] == 'debug':
    envi = request.config.getoption('--envi')
    if envi == 'debug':
        print('2')
        print(envi)
        path = os.path.abspath(__file__)
        data = GetData(path, 'debug').get_test_data()
        print(data)
    assert  1 == 1

