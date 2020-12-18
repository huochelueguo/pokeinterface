# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:test_unfollow_user.py
@Time:NAME.py@Time:2020/12/18 16:49
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


class Test_Unfollow(object):

    @pytest.mark.run(2)
    @allure.feature('用户粉丝&关注相关case')
    @allure.story('用户取消关注用户')
    @allure.step('登录获取到token后，使用token访问接口，取消关注用户')
    @allure.title('{unfollow_user[0]}')
    @allure.severity('critical')  # 用例优先级
    def test_unfollow(self, get_config, get_fans_token, unfollow_user):
        test_url = get_config[0] + unfollow_user[1].get('path')
        test_header = unfollow_user[1].get('header')
        test_header['Cookie'] = get_fans_token[0]
        test_data = unfollow_user[1].get('body')
        res = Post(url=test_url, header=test_header, data=test_data).post_request()
        res_data = res[0]
        res_code = res[1]
        def_name = sys._getframe().f_code.co_name
        logger.info(f'进行数据对比{def_name}\n')
        assert unfollow_user[2].get('code') == res_code
        assert unfollow_user[2].get('relation') == jsonpath.jsonpath(res_data, '$..relation')[0]



