# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:conftest.py
@Time:2020/9/23 下午11:21
"""
import pytest
import os

from commom.GetYaml import GetData
from commom.Logs import Log

# 调用日志模块
log = Log(__name__)
logger = log.Logger


def pytest_generate_tests(metafunc):
    # 当前工作目录路径
    dir_path = os.path.split(__file__)
    if 'empty_login' in metafunc.fixturenames:
        # 读取数据的路径
        data_path = os.path.join(dir_path[0], 'test_empty_phone')
        # 判断环境，获取不同环境数据
        if metafunc.config.getoption('--envi') == 'debug':
            test_data = GetData(path=data_path, envi='debug').get_data()
            metafunc.parametrize('empty_login', test_data[1], ids=test_data[0])
            logger.info('返回参数化数据【空手机号码+正确的密码】')
        elif metafunc.config.getoption('--envi') == 'online':
            test_data = GetData(path=data_path, envi='online').get_data()
            metafunc.parametrize('empty_login', test_data[1], ids=test_data[0])
            logger.info('返回参数化数据【空手机号码+正确的密码】')
    if 'right_login' in metafunc.fixturenames:
        data_path = os.path.join(dir_path[0] , 'test_right_phone')
        if metafunc.config.getoption('--envi') == 'debug':
            test_data = GetData(path=data_path, envi='debug').get_data()
            print(type(test_data[1]),test_data[1])
            print(type(test_data[0]),test_data[0])
            metafunc.parametrize('right_login', test_data[1], ids=test_data[0])
            logger.info('返回参数化数据【正确手机号+正确的密码】')
        elif metafunc.config.getoption('--envi') == 'online':
            test_data = GetData(path=data_path, envi='online').get_data()
            metafunc.parametrize('right_login', test_data[1], ids=test_data[0])
            logger.info('返回参数化数据【正确手机号+正确的密码】')
    if 'empty_password' in metafunc.fixturenames:
        data_path = os.path.join(dir_path[0], 'test_empty_password')
        if metafunc.config.getoption('--envi') == 'debug':
            test_data = GetData(path=data_path, envi='debug').get_data()
            metafunc.parametrize('empty_password', test_data[1], ids=test_data[0])
            logger.info('返回参数化数据【正确手机号+空的密码】')
        if metafunc.config.getoption('--envi') == 'online':
            test_data = GetData(path=data_path, envi='online').get_data()
            metafunc.paramerrize('empty_password', test_data[0], ids=test_data[1])
            logger.info('返回参数化数据【正确手机号+空的密码】')







