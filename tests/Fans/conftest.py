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
from commom.Logs import Log

# 调用日志模块
log = Log(__name__)
logger = log.Logger
PATH = os.path.split(__file__)[0]
DATA_PATH = os.path.join(PATH, 'test_get_fans')
DATA_PATH_ZERO = os.path.join(PATH, 'test_get_fans_zero')


@pytest.fixture(scope='class')
def get_fans_token(get_config):
    # 根据主conftest中的getconfig读取环境配置信息
    if get_config[1] == 'debug':
        debug_data = GetData(path=DATA_PATH, envi='debug').get_data()
        login_data = debug_data[1][0][1]  # 读取数据中切割出登录所使用的数据
        token = ReturnToken(url=login_data.get('path'), data=login_data.get('body'),
                            header=login_data.get('headers')).post_request()    # 使用数据登录返回token和uid
        # print(token)
    elif get_config[1] == 'online':
        online_data = GetData(path=DATA_PATH, envi='online').get_data()
        login_data = online_data[1][0][1]  # 读取数据中切割出登录所使用的数据
        token = ReturnToken(url=login_data.get('path'), data=login_data.get('body'),
                            header=login_data.get('headers')).post_request()
    yield token


@pytest.fixture(scope='class')
def get_fans_zero_token(get_config):
    # 根据主conftest中的getconfig读取环境配置信息
    if get_config[1] == 'debug':
        debug_data_zero = GetData(path=DATA_PATH_ZERO, envi='debug').get_data()
        login_data = debug_data_zero[1][0][1]  # 读取数据中切割出登录所使用的数据
        token = ReturnToken(url=login_data.get('path'), data=login_data.get('body'),
                            header=login_data.get('headers')).post_request()  # 使用数据登录返回token和uid
    elif get_config[1] == 'online':
        online_data_zero = GetData(path=DATA_PATH_ZERO, envi='online').get_data()
        login_data = online_data_zero[1][0][1]  # 读取数据中切割出登录所使用的数据
        token = ReturnToken(url=login_data.get('path'), data=login_data.get('body'),
                            header=login_data.get('headers')).post_request()
    yield token


def pytest_generate_tests(metafunc):
    # todo:目前取值为写死的，无法进行参数化，如果多组测试数据，token和对应组怎么插入
    global test_data
    if 'get_fans' in metafunc.fixturenames:
        if metafunc.config.getoption('--envi') == 'debug':
            debug_data = GetData(path=DATA_PATH, envi='debug').get_data()
            test_data_ids = debug_data[0][1::]
            test_data = debug_data[1][1::]
            metafunc.parametrize('get_fans', test_data, ids=test_data_ids)
            logger.info('返回参数化数据【用户粉丝数非0的情况】')
        elif metafunc.config.getoption('--envi') == 'online':
            online_data = GetData(path=DATA_PATH, envi='online').get_data()
            test_data_ids = online_data[0][1].split()
            test_data = online_data[1][1::]
            metafunc.parametrize('get_fans', test_data, ids=test_data_ids)
            logger.info('返回参数化数据【用户粉丝数非0的情况】')
    if 'get_fans_zero' in metafunc.fixturenames:
        if metafunc.config.getoption('--envi') == 'debug':
            debug_data_zero = GetData(path=DATA_PATH_ZERO, envi='debug').get_data()
            test_data_ids = debug_data_zero[0][1].split()
            test_data = debug_data_zero[1][1::]
            metafunc.parametrize('get_fans_zero', test_data, ids=test_data_ids)
            logger.info('返回参数化数据【用户粉丝数为0的情况】')
        elif metafunc.config.getoption('--envi') == 'online':
            online_data_zero = GetData(path=DATA_PATH_ZERO, envi='online').get_data()
            test_data_ids = online_data_zero[0][1].split()
            test_data = online_data_zero[1][1::]
            metafunc.parametrize('get_fans_zero', test_data, ids=test_data_ids)
            logger.info('返回参数化数据【用户粉丝数为0的情况】')
    if 'followers_zero' in metafunc.fixturenames:
        data_path = os.path.join(PATH + '/test_followers_zero')
        if metafunc.config.getoption('--envi') == 'debug':
            test_data = GetData(path=data_path, envi='debug').get_data()
            metafunc.parametrize('followers_zero', test_data[1], ids=test_data[0])
            logger.info('返回参数化数据【用户0关注情况】')
        elif metafunc.config.getoption('--envi') == 'online':
            test_data = GetData(path=data_path, envi='online').get_data()
            metafunc.parametrize('followers_zero', test_data[1], ids=test_data[0])
            logger.info('返回参数化数据【用户0关注情况】')
    if 'followers_not_zero' in metafunc.fixturenames:
        data_path = os.path.join(PATH + '/test_follower_not_zero')
        if metafunc.config.getoption('--envi') == 'debug':
            test_data = GetData(path=data_path, envi='debug').get_data()
        elif metafunc.config.getoption('--envi') == 'online':
            test_data = GetData(path=data_path, envi='online').get_data()
        metafunc.parametrize('followers_not_zero', test_data[1], ids=test_data[0])
        logger.info('返回参数化数据【用户非0关注情况】')
    if 'follow_user' in metafunc.fixturenames:
        data_path = os.path.join(PATH + '/test_follow_user')
        if metafunc.config.getoption('--envi') == 'debug':
            test_data = GetData(path=data_path, envi='debug').get_data()
        elif metafunc.config.getoption('--envi') == 'online':
            test_data = GetData(path=data_path, envi='online').get_data()
        metafunc.parametrize('follow_user', test_data[1], ids=test_data[0])
        logger.info('返回参数化数据【关注用户】')
    if 'unfollow_user' in metafunc.fixturenames:
        data_path = os.path.join(PATH + '/test_unfollow_user')
        if metafunc.config.getoption('--envi') == 'debug':
            test_data = GetData(path=data_path, envi='debug').get_data()
        elif metafunc.config.getoption('--envi') == 'online':
            test_data = GetData(path=data_path, envi='online').get_data()
        metafunc.parametrize('unfollow_user', test_data[1], ids=test_data[0])
        logger.info('返回参数化数据【取消关注】')


def test_one(unfollow_user):
    a = unfollow_user[1]
    # print(get_fans.get('path'))
    print(a)
    assert 1 == 1
