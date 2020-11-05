# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:test_empty_phone.py
@Time:2020/9/7 上午9:48
@手机号为空时发送请求
"""

import pytest

from commom.RequestPost import Post



class Test_Empty(object):
    """

    """

    def test_empty_phone(self, empty_login, get_config):
        test_url = get_config[0] + empty_login[1].get('path')
        test_header = empty_login[1].get('headers')
        test_body = empty_login[1].get('body')
        res = Post(url=test_url, header=test_header, body=test_body).post_request()[0]
        res_code = Post(url=test_url, header=test_header, body=test_body).post_request()[1]
        # print(res)
        # print(res_code)
        # print(empty_login[2].get('code'))
        assert 500 == res_code
        assert empty_login[2].get('err_msg') == res.get('err_msg')
