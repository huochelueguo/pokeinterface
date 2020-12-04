# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:test_fans_assert2.py
@Time:2020/12/3 上午9:44
对比第一页最后一条数据和第二页第一条数据，应该不是同一个用户，防止翻页时下发数据错误【曾经出现过该错误】
"""
# 大致思路：通过test_get_fans获取的返回值，写入到某个特定文件中，之后再本文件中对两次写入值进行对比，看最后一条和第一条是否一致
# 因此这两条需要配置一下顺序，必须先让test_get_fans执行，否则没有值无法对比
import os
import allure
import pytest

from commom.GetPath import Right_Path


class Test_Fans_Assert(object):

    def test_assert(self, get_config):
        root_path = Right_Path().root_path()
        if get_config[1] == 'debug':
            debug_path = '/datas/debug/Fans/test_fans_assert'
            fans_data_path = root_path + debug_path
        else:
            debug_path = 'datas/online/Fans/test_fans_assert'
            fans_data_path = root_path + debug_path
        with open(fans_data_path, 'r') as f:
            data = f.read()
            if data == '':
                pytest.xfail(reason='文件为空，无法进行对比，用例执行中止')
            else:
                print(type(data),data)
