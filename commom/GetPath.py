# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:GetPath.py
@Time:2020/11/18 下午11:49
"""
# 返回准确的路径，达到不同设备，不因为路径导致输出错误
import os


class Right_Path(object):
    """通过2次分割获取工程根目录"""
    @staticmethod
    def root_path():
        one_spilt = os.path.split(__file__)[0]
        two_spilt = os.path.split(one_spilt)[0]
        root_path = two_spilt
        return root_path


if __name__ == '__main__':
    a = Right_Path().root_path()
    print(a)