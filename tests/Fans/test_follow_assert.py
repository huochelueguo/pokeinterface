# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:test_follow_assert.py
@Time:NAME.py@Time:2020/12/18 20:53
@ 验证我的关注，两页数据下发准确，防止翻页时下发数据错误【曾经出现过该错误】
"""

import sys
import allure
import pytest



from commom.Logs import Log
from commom.GetPath import Right_Path

log = Log(__name__)
logger = log.Logger


class Test_Followings_Not_Zero(object):
    @allure.feature('用户粉丝&关注相关case')
    @allure.story('用户有关注的情况')
    @allure.step('登录获取到token后，使用token访问接口，获取关注数')
    @allure.title('用户第一页最后一个数据和第二页第一个进行比对，应该不一致')
    @allure.severity('critical')  # 用例优先级
    @pytest.mark.run(order=2)
    def test_assert_follow(self, get_config):
        global assert_data_path
        root_path = Right_Path().root_path()
        if get_config[1] == 'debug':
            dubug_path = '/datas/debug/Fans/test_follow_assert'
            assert_data_path = root_path + dubug_path
            # print(assert_data_path)
        elif get_config[1] == 'online':
            online_path = '/datas/online/Fans/test_follow_assert'
            assert_data_path = root_path + online_path
        with open(assert_data_path, 'r+', encoding='utf-8') as f:
            data = f.readlines()
            if not data:
                # print('文件为空,无关注uid,无法比对,中止用例')
                logger.error('文件为空,无关注uid,无法比对,中止用例')
                pytest.mark.xfail(reason='文件为空,无关注uid,无法比对,中止用例')
            else:
                uid1 = data[0][:-1]
                uid2 = data[1]
                def_name = sys._getframe().f_code.co_name
                logger.info(f'进行数据对比{def_name}\n')
                assert uid1 != uid2
                f.seek(0)
                f.truncate()
                logger.info(f'{def_name}清空数据\n')

