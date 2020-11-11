# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:test_right_phone.py
@Time:2020/8/26 上午9:33
"""
# 通过pytest.ini读取测试环境---通过主路径下的conftest读取对应环境的URL---通过子目录中的conftest读取数据---本文件中读取conftest中的fixture后进行测试
import allure
import os
import sys
import pytest

from commom.RequestPost import Post
from commom.Logs import Log

# 调用日志模块
log = Log(__name__)
logger = log.Logger


class Test_Login(object):

    @allure.feature('手机号码登录')   # 用例模块名称
    @allure.story('正确的手机号和密码')  # 标注Features功能模块下的分支功能
    @allure.severity('critical')    # 用例优先级
    @allure.step('获取手机号及对应密码后，提交登录')    # 用例每一步说明
    @allure.title('正确手机号及密码登录')     # 用例标题
    def test_right_login(self, right_login, get_config):
        """
        用例描述：使用正确的手机号码和密码登录
        """
        test_url = get_config[0] + right_login[1].get('path')
        test_header = right_login[1].get('headers')
        test_body = right_login[1].get('body')
        def_name = sys._getframe().f_code.co_name
        logger.info("开始执行脚本%s:\n", def_name)
        res = Post(url=test_url, header=test_header, body=test_body).post_request()[0]
        res_code = Post(url=test_url, header=test_header, body=test_body).post_request()[1]
        test_body = right_login[1].get('body')
        print(right_login[0])
        print(right_login[1])
        print(right_login[2])
        logger.info(f'进行数据对比{def_name}\n')
        assert right_login[2].get('code') == res_code
        assert right_login[2].get('err_msg') == res.get('err_msg')



