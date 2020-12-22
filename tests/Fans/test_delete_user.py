# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:test_delete_user.py
@Time:NAME.py@Time:2020/12/22 18:01
@ 删除用户：客户端逻辑为仅能删除已注销用户
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


class Test_Delete_User(object):
    @pytest.mark.run(order=2)
    @allure.feature('用户粉丝&关注相关case')
    @allure.story('删除其他用户')
    @allure.step('登录获取到token后，使用token访问接口，删除数据中的t_uid用户')
    @allure.title('{delete_user[0]}')
    @allure.severity('critical')  # 用例优先级
    # 注意： 本用例和test_get_fans使用同一个账号，共同使用conftest/中的get_fans_token
    def test_delete(self, get_config, get_fans_token, delete_user):
        test_url = get_config[0] + delete_user[1].get('path')
        test_header = delete_user[1].get('header')
        test_header['Cookie'] = get_fans_token[0]
        test_data = delete_user[1].get('body')
        res = Post(url=test_url, header=test_header, data=test_data).post_request()
        res_data = res[0]
        res_code = res[1]
        def_name = sys._getframe().f_code.co_name
        logger.info(f'进行数据对比{def_name}\n')
        # 开始启用pytest.assume断言
        pytest.assume(res_code == delete_user[2].get('code'))
        pytest.assume(res_data.get('err_msg') == delete_user[2].get('err_msg'))
        pytest.assume(jsonpath.jsonpath(res_data, '$..relation')[0] == delete_user[2].get('relation'))
        logger.info('删除用户case执行完成')