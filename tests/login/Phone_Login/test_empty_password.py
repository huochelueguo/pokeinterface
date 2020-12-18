# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:test_empty_password.py
@Time:NAME.py@Time:2020/11/6 16:19
"""
# 密码为空时请求数据
import sys

import allure
import pytest

from commom.Logs import Log
from commom.RequestPost import Post


# 调用日志模块
log = Log(__name__)
logger = log.Logger


class Test_Password(object):

    @allure.feature('手机号码登录')
    @allure.story('手机号码+空的密码')
    @allure.severity('critical')
    @allure.title('{empty_password[0]}')
    def test_empty_password(self, get_config, empty_password):
        """
        用例描述：使用正确的手机号码和空的密码登录
        :param get_config: 读取conftest配置，获得环境
        :param empty_password: 获取参数化数据
        :return:
        """
        def_name = sys._getframe().f_code.co_name
        logger.info("开始执行脚本%s:", def_name)
        test_url = get_config[0] + empty_password[1].get('path')
        test_body = empty_password[1].get('body')
        test_header = empty_password[1].get('headers')
        res = Post(url=test_url, header=test_header, json=test_body).post_request()[0]
        logger.info(f'进行数据对比{def_name}\n')
        assert empty_password[2].get('code') == res.get('error_code')
        assert empty_password[2].get('err_msg') == res.get('err_msg')

