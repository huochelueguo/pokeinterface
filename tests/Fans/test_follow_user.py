# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:test_follow_user.py
@Time:NAME.py@Time:2020/12/18 15:05
@ 关注用户：非官方账号
"""
import sys
import pytest
import allure
import jsonpath
from commom.Logs import Log
from commom.RequestPost import Post

# 调用日志模块
log = Log(__name__)
logger = log.Logger


class Test_Follow(object):
    # 使用非0关注用户，继续关注
    @allure.feature('用户粉丝&关注相关case')
    @allure.story('用户关注其他用户')
    @allure.step('登录获取到token后，使用token访问接口，关注其他用户')
    @allure.title('{follow_user[0]}')
    @allure.severity('critical')  # 用例优先级
    @pytest.mark.run(1)
    def test_follow_user(self, get_config, get_fans_token, follow_user):
        test_url = get_config[0] + follow_user[1].get('path')
        test_header = follow_user[1].get('header')
        test_header['Cookie'] = get_fans_token[0]
        test_data = follow_user[1].get('body')
        res = Post(url=test_url, header=test_header, data=test_data).post_request()
        res_data = res[0]
        res_code = res[1]
        def_name = sys._getframe().f_code.co_name
        logger.info(f'进行数据对比{def_name}\n')
        assert follow_user[2].get('code') == res_code
        assert follow_user[2].get('relation') != jsonpath.jsonpath(res_data, '$..relation')[0]