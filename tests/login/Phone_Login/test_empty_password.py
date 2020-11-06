# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:test_empty_password.py
@Time:NAME.py@Time:2020/11/6 16:19
"""
# 密码为空时请求数据

import pytest

from commom.RequestPost import Post


class Test_Password(object):

    def test_empty_password(self, get_config, empty_password):

        test_url = get_config[0] + empty_password[1].get('path')
        test_body = empty_password[1].get('body')
        test_header = empty_password[1].get('headers')
        res = Post(url=test_url, header=test_header, body=test_body).post_request()[0]
        assert empty_password[2].get('code') == res.get('error_code')
        assert empty_password[2].get('err_msg') == res.get('err_msg')

