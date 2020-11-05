# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:ReadConfig.py
@Time:2020/8/13 上午9:01
"""

# 配置文件读取，返回对应值
import yaml
import os


class ReadConfig(object):

    # 获取当前文件的绝对路径，拼接上config文件，使读取中不使用相对路径
    def __init__(self):
        path = os.path.split(__file__)
        self.confpath = path[0] + '/config'
        print(self.confpath)
        # print(type(self.configpath))

    # 读取config.yaml数据返回
    def get_data(self):
        try:
            with open(self.confpath, 'r', encoding='utf-8') as f:
                data = yaml.load(f, Loader=yaml.FullLoader)
        except Exception as result:
            print(f'错误： {result}')
        else:
            return data

    # 读取返回数据中的环境配置文件
    def get_envi(self, env):
        # print(self.get_data())
        try:
            urllist = self.get_data().get(env)
            url = urllist[0]
            return url.get('url')
        except Exception as result:
            print(f'错误： {result}')


if __name__ == '__main__':
    data = ReadConfig().get_envi('debug')
    print(data)
    print(type(data))
    a = ReadConfig().confpath
