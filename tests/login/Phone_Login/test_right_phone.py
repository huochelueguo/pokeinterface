# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:test_right_phone.py
@Time:2020/8/26 上午9:33
"""
# 通过pytest.ini读取测试环境---通过主路径下的conftest读取对应环境的URL---通过子目录中的conftest读取数据---本文件中读取conftest中的fixture后进行测试

import pytest

from commom.RequestPost import Post


class Test_Login(object):

    def test_right_login(self, right_login, get_config):

        test_url = get_config[0] + right_login[1].get('path')
        test_header = right_login[1].get('headers')
        test_body = right_login[1].get('body')
        res = Post(url=test_url, header=test_header, body=test_body).post_request()[0]
        res_code = Post(url=test_url, header=test_header, body=test_body).post_request()[1]
        test_body = right_login[1].get('body')
        print(right_login[0])
        print(right_login[1])
        print(right_login[2])
        assert right_login[2].get('code') == res_code
        assert right_login[2].get('err_msg') == res.get('err_msg')



