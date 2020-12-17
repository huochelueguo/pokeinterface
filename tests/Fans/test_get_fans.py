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
import os
import sys
import allure
import jsonpath
import pytest

from commom.RequestGet import Get
from commom.Logs import Log
from commom.GetPath import Right_Path

# 调用日志模块
log = Log(__name__)
logger = log.Logger


class Test_Fans(object):

    @allure.feature('用户粉丝数相关case')
    @allure.story('用户粉丝数非0的情况')
    @allure.step('登录获取到token后，使用token访问接口，获取粉丝数')
    @allure.title('非0的粉丝用户')
    @allure.severity('critical')  # 用例优先级
    @pytest.mark.run(order=1)
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
        # print(res_data)
        def_name = sys._getframe().f_code.co_name
        logger.info(f'进行数据对比{def_name}\n')
        assert get_fans[2].get('code') == res_code
        if test_params.get('page_index') < 9999:
            assert get_fans[2].get('data') != res[0].get('data').get('users')
            logger.info('将服务端返回结果存入test_fans_assert')
            # 将两页的结果分别存入test_fans_asser中，为了在test_fanse_assert中对比两页最后和第一个用户是否一致
            root_path = Right_Path().root_path()
            if get_config[1] == 'debug':
                debug_path = '/datas/debug/Fans/test_fans_assert'
                fans_data_path = root_path + debug_path
            else:
                debug_path = 'datas/online/Fans/test_fans_assert'
                fans_data_path = root_path + debug_path
            with open(fans_data_path, 'a') as f:
                # uid = res_data.get('data').get('users')[::-1][0].get('user').get('uid')
                # 使用jsonpath替代原来的定位方法
                uid = jsonpath.jsonpath(res_data, '$..uid')[-1]
                str_uid = str(uid)
                f.write(str_uid + '\n')
        else:
            assert get_fans[2].get('data').get('has_more') == res_data.get('data').get('has_more')
