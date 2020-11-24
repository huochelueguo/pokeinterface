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
# 2.对数据进行拆分，抓取出登录需要的数据，调用gettoken方法，获取到token
# 3.再使用pytest.generate.tests对case进行参数化
import os
import pytest
from commom.GetToken import ReturnToken
from commom.RequestGet import Get
from commom.GetYaml import GetData
from commom.Logs import Log

# 调用日志模块
log = Log(__name__)
logger = log.Logger


class Test_Fans(object):

    def test_get_fans(self, get_fans, get_fans_token, get_config):
        # test_url = get_config[0] + get_fans[1].get('path')
        print(get_config[0])
        print(get_fans[1].get('path'))
        assert 1 == 1



