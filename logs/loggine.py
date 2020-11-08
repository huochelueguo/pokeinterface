# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:loggine.py
@Time:NAME.py@Time:2020/11/7 17:59
"""
import logging

logging.basicConfig(format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                    level=logging.DEBUG,
                    filename='test.log',
                    filemode='a')
fh = logging.FileHandler('test.log', encoding='utf-8')
logging.debug('debug级别，一般用来打印一些调试信息，级别最低')
logging.info('info级别，一般用来打印一些正常的操作信息')
logging.warning('waring级别，一般用来打印警告信息')
logging.error('error级别，一般用来打印一些错误信息')
logging.critical('critical级别，一般用来打印一些致命的错误信息，等级最高')