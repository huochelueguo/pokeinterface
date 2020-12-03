# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:test_get_fans_zero.py
@Time:2020/11/25 上午9:35
"""
# 无粉丝用户返回值验证
import os
import sys
import allure
from commom.RequestGet import Get
from commom.Logs import Log


log = Log(__name__)
logger = log.Logger


class Test_Fans_Zero(object):

    @allure.feature('用户粉丝数相关case')
    @allure.story('用户粉丝数为0的情况')
    @allure.step('登录获取到token后，使用token访问接口，获取粉丝数')
    @allure.title('无粉丝用户')
    @allure.severity('critical')  # 用例优先级
    def test_fans_zero(self, get_config, get_fans_zero_token, get_fans_zero):
        """
        :param get_config: 获取环境配置
        :param get_fans_zero_token: 获取用户token和uid
        :param get_fans_zero: 获取参数化数据
        :return:
        """
        url = get_config[0] + get_fans_zero[1].get('path')
        test_header = get_fans_zero[1].get('header')
        test_header['Cookie'] = get_fans_zero_token[0]
        test_params = get_fans_zero[1].get('params')
        test_params['t_uid'] = get_fans_zero_token[1]
        res = Get(url=url, params=test_params, header=test_header).get_request()
        print(res)
        def_name = sys._getframe().f_code.co_name
        logger.info(f'进行数据对比{def_name}\n')
        assert get_fans_zero[2].get('code') == 200
        assert get_fans_zero[2].get('data') == res[0].get('data').get('users')
