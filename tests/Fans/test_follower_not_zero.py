# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:test_follower_not_zero.py
@Time:NAME.py@Time:2020/12/16 14:48
@ 用户关注非0的情况，第一个关注应该不是poke子
"""
import json
import sys
import allure
import jsonpath
import pytest

from commom.RequestGet import Get
from commom.Logs import Log


log = Log(__name__)
logger = log.Logger


class Test_Followings_Not_Zero(object):
    @allure.feature('用户关注相关case')
    @allure.story('用户有关注的情况')
    @allure.step('登录获取到token后，使用token访问接口，获取粉丝数')
    @allure.title('{followers_not_zero[0]}')
    # @allure.title('关注：非0关注情况')
    @allure.severity('critical')  # 用例优先级
    # 注意： 本用例和test_get_fans使用同一个账号，共同使用conftest/中的get_fans_token
    def test_followings_not_zero(self, get_config, followers_not_zero, get_fans_token):
        test_url = get_config[0] + followers_not_zero[1].get('path')
        test_data = list(followers_not_zero)
        test_header = followers_not_zero[1].get('header')
        test_header['Cookie'] = get_fans_token[0]
        test_params = test_data[1].get('params')
        test_params['t_uid'] = get_fans_token[1]
        test_params = test_data[1].get('params')
        res = Get(url=test_url, params=test_params, header=test_header).get_request()
        res_data = res[0]
        res_code = res[1]
        # print(res[0])
        print(followers_not_zero[2].get('data').get('has_more'))
        def_name = sys._getframe().f_code.co_name
        logger.info(f'进行数据对比{def_name}\n')
        assert followers_not_zero[2].get('code') == res_code
        assert followers_not_zero[2].get('data').get('has_more') == res_data.get('data').get('has_more')


