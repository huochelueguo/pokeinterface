# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:test_followers_zero.py
@Time:2020/12/8 上午9:00
@用户关注为0的情况：应当默认关注poke子
 注意：粉丝为0和关注数为0共用的一个新用户，同一个获取token前置方法
"""
import os
import sys
import allure
import jsonpath

from commom.RequestGet import Get
from commom.Logs import Log


log = Log(__name__)
logger = log.Logger


class Test_Follwoers_Zero(object):
    @allure.feature('')
    @allure.story('')
    @allure.step('登录获取到token后，使用token访问接口，获取粉丝数')
    @allure.title('关注：0关注情况')
    @allure.severity('critical')  # 用例优先级
    def test_zero(self, get_config, get_fans_zero_token, followers_zero):
        test_url = get_config[0] + followers_zero[1].get('path')
        print(test_url)
        test_data = list(followers_zero)
        test_header = test_data[1].get('header')
        test_header['Cookie'] = get_fans_zero_token[0]
        test_params = test_data[1].get('params')
        test_params['t_uid'] = get_fans_zero_token[1]
        res = Get(url=test_url, params=test_params, header=test_header).get_request()
        res_data = res[0]
        res_code = res[1]
        print(res_data)
        assert_data = jsonpath.jsonpath(res_data, '$..uid')
        # 关注为0，默认关注poke子，根据这个来进行对比
        def_name = sys._getframe().f_code.co_name
        logger.info(f'进行数据对比{def_name}\n')
        assert followers_zero[2].get('code') == res_code
        assert assert_data[0] == 'u1000000000000000000'
        assert len(assert_data) == 1



