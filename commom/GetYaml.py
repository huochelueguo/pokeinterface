# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:GetYaml.py
@Time:2020/8/24 上午9:33
"""
# 从yaml读取数据的封装
import yaml
import os
from commom.Logs import Log

# 调用日志模块
log = Log(__name__)
logger = log.Logger


class GetData(object):

    """
    封装获取数据方法
    case   # 存储测试用例名称
    http   # 存储请求对象
    expected  # 存储预期结果
    """

    def __init__(self, path, envi):
        """
        将文件路径替换为数据存储文件路径
        :param path: 读取文件路径
        :param envi: 读取环境
        """
        path_yaml = os.path.splitext(path)
        path_data = path_yaml[0].replace('tests', 'datas', 1)
        self.path = path_data
        self.envi = envi

    def get_data(self):
        """通过在conftest中输入的envi判断是环境，读取对应环境中的数据"""
        if self.envi == 'debug':
            return self.get_test_data()
        elif self.envi == 'online':
            return self.get_online_data()
        else:
            print('输入内容错误，请检查')

    def get_test_data(self):
        """由于数据分测试/线上环境，因此需要再次调整对应路径"""
        case = []
        http = []
        expected = []
        test_path_data = self.path.replace('datas', 'datas/debug')
        try:
            with open(test_path_data, 'r', encoding='utf-8') as f:
                data = yaml.load(f, Loader=yaml.FullLoader)
                data_list = data.get('tests')
                # 遍历每个用例，对应数据插入列表中
                for td in data_list:
                    case.append(td.get('desc'))
                    http.append(td.get('http'))
                    expected.append(td.get('expected'))
                    test_data = zip(case, http, expected)
                    test_data_list = list(test_data)
                logger.info('返回测试数据【测试环境】')
                return case, test_data_list
        except Exception as result:
            print(result)
            logger.error(f'{result}')

    def get_online_data(self):
        case = []
        http = []
        expected = []
        online_path_data = self.path.replace('datas', 'datas/online')
        try:
            with open(online_path_data, 'r', encoding='utf-8') as f:
                data = yaml.load(f, Loader=yaml.FullLoader)
                data_list = data.get('tests')
                for od in data_list:
                    case.append(od.get('desc'))
                    http.append(od.get('http'))
                    expected.append(od.get('expected'))
                online_data = list(zip(case, http, expected))
                logger.info('返回测试数据【线上环境】')
                return case, online_data
        except Exception as result:
            print(result)
            logger.error(f'{result}')






if __name__ == '__main__':
    # mac
    #(['正确的密码', '正确的密码2'], [('正确的密码', {'path': '/api/user/login', 'headers': '', 'body': {'platform': 4, 'token': 'login', 'id_token': '+8618515588536', 'secret': '111111'}}, {'code': 200, 'err_msg': 'success'}), ('正确的密码2', {'path': '/api/user/login', 'headers': '', 'body': {'platform': 4, 'token': 'login', 'id_token': '+8618515588536', 'secret': '111111'}}, {'code': 200, 'err_msg': 'success'})])

    # path = '/Users/sunwenxiao/PycharmProjects/poketinterface/tests/Login/Phone_Login/test_right_phone.py'
    path = '/Users/sunwenxiao/PycharmProjects/pokeinterfacetest/tests/Fans/test_get_fans.py'
    a = GetData(path, envi='debug').get_test_data()
    print(a)
    print(type(a))
