# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:test_empty_phone.py
@Time:2020/9/7 上午9:48
@手机号为空时发送请求
"""
import sys

import allure
import pytest

from commom.Logs import Log
from commom.RequestPost import Post


log = Log(__name__)
logger = log.Logger


class Test_Empty(object):
    """

    """

    @allure.feature('手机号码登录')
    @allure.story('空手机号码+正确的密码')
    @allure.severity('critical')
    def test_empty_phone(self, empty_login, get_config):
        """
        用例描述：使用空的手机号码+非空密码登录
        :param empty_login: 读取conftest配置，获得环境
        :param get_config: 获取参数化数据
        :return:
        """
        def_name = sys._getframe().f_code.co_name
        logger.info("开始执行脚本%s:", def_name)
        test_url = get_config[0] + empty_login[1].get('path')
        test_header = empty_login[1].get('headers')
        test_body = empty_login[1].get('body')
        res = Post(url=test_url, header=test_header, data=test_body).post_request()
        res_data = res[0]
        res_code = res[1]
        # print(res)
        # print(res_code)
        # print(empty_login[2].get('code'))
        logger.info(f'进行数据对比{def_name}\n')
        assert 500 == res_code
        assert empty_login[2].get('err_msg') == res_data.get('err_msg')
