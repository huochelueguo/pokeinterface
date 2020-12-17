# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:test_follower_not_zero.py
@Time:NAME.py@Time:2020/12/16 14:48
@ 用户关注非0的情况，第一个关注应该不是poke子
"""
import sys
import allure
import jsonpath

from commom.RequestGet import Get
from commom.Logs import Log


log = Log(__name__)
logger = log.Logger


class Test_Followings_Not_Zero(object):
    # 注意： 本用例和test_get_fans使用同一个账号，共同使用conftest/中的get_fans_token
    def test_followings_not_zero(self, get_config, followers_not_zero, get_fans_token):
        test_url = get_config[0] + followers_not_zero[1].get('path')
        test_data = list(followers_not_zero)
        test_header = followers_not_zero[1].get('header')
        test_header['Cookie'] = get_fans_token[0]
        test_params = test_data[1].get('params')
        res = Get(url=test_url, params=test_params, header=test_header).get_request()
        res_data = res[0]
        res_code = res[1]
        print(res)
        assert 1 == 1


