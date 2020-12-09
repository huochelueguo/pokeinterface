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
import time
import allure
import pytest
import sys
from commom.Logs import Log
from commom.GetPath import Right_Path

# 调用日志模块
log = Log(__name__)
logger = log.Logger


class Test_Fans_Assert(object):

    @allure.feature('用户粉丝数相关case')
    @allure.story('用户粉丝数非0的情况')
    @allure.step('通过test_get_fans获取两页数据，将第一页最后一位数据和第二页第一位进行对比')
    @allure.title('核对两页下发数据不一致')
    @allure.severity('critical')  # 用例优先级
    @pytest.mark.run(order=2)  # 因为只有test_get_fans运行后才有数据，因此要把该用例顺序后置，正数>无符号>负数
    def test_assert(self, get_config):
        root_path = Right_Path().root_path()
        if get_config[1] == 'debug':
            debug_path = '/datas/debug/Fans/test_fans_assert'
            fans_data_path = root_path + debug_path
        else:
            debug_path = 'datas/online/Fans/test_fans_assert'
            fans_data_path = root_path + debug_path
        with open(fans_data_path, 'r+') as f:
            data = f.readlines()
            if not data:
                logger.error('粉丝uid文件为空，无法进行对比')
                pytest.xfail(reason='文件为空，无法进行对比，用例执行中止')
            else:
                line1 = data[0][:-1]
                line2 = data[1]
                def_name = sys._getframe().f_code.co_name
                logger.info(f'进行数据对比{def_name}\n')
                assert line1 != line2
                # time.sleep(3)
                # print(line1,line2)
                # 对比完成，清空内容，为下次写入做准备
                f.seek(0)
                f.truncate()
                logger.info(f'{def_name}清空数据\n')


