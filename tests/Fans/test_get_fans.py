# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:test_get_fans.py
@Time:2020/11/17 上午9:17
"""
# 尝试编写使用token的接口，整体流程：
# 1.conftest中创建一个fixture,该fixture先通过主fixture获取环境配置，根据环境配置读取数据
# 2.对数据进行拆分，抓取出登录需要的数据，调用gettoken方法，获取到token/uid
# 3.再使用pytest.generate.tests对case进行参数化，使用数据进行get请求
import sys
import allure
from commom.RequestGet import Get
from commom.Logs import Log

# 调用日志模块
log = Log(__name__)
logger = log.Logger


class Test_Fans(object):

    @allure.feature('用户粉丝数相关case')
    @allure.story('用户粉丝数非0的情况')
    @allure.step('登录获取到token后，使用token访问接口，获取粉丝数')
    @allure.title('非0的粉丝用户')
    def test_get_fans(self, get_fans_token, get_config, get_fans):
        """
        :param get_fans_token: 返回登录用户token/uid
        :param get_config: 获取环境配置：测试/线上
        :param get_fans: 获取访问接口所需数据
        :return:
        """
        test_url = get_config[0] + get_fans[1].get('path')
        test_data = list(get_fans)
        test_header = test_data[1].get('header')
        test_header['Cookie'] = get_fans_token[0]
        test_params = test_data[1].get('params')
        test_params['t_uid'] = get_fans_token[1]
        res = Get(url=test_url, params=test_params, header=test_header).get_request()
        res_data = res[0]
        res_code = res[1]
        # print(test_url)
        # print(test_header)
        # print(test_params)
        print(res)
        def_name = sys._getframe().f_code.co_name
        logger.info(f'进行数据对比{def_name}\n')
        assert get_fans[2].get('code') == res_code
        assert get_fans[2].get('data') != res[0].get('data').get('users')



