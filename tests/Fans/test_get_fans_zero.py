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
import allure
import pytest
from commom.RequestGet import Get
from commom.Logs import Log


log = Log(__name__)
logger = log.Logger


class Test_Fans_Zero(object):

    @allure.feature('用户粉丝数相关case')
    @allure.story('用户粉丝数为0的情况')
    @allure.step('登录获取到token后，使用token访问接口，获取粉丝数')
    @allure.title('为0的粉丝用户')
    def test_fans_zero(self, get_config, get_fans_zero, get_fans_token):
        a = get_fans_token
        print(a)
        assert 1 ==1