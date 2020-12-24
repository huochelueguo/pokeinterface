# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:PokeConst.py
@Time:2020/12/23 下午11:53
"""

from commom import Const
Const.MP4_NUM = '1'
Const.M4A_NUM = '2'
Const.JPG_NUM = '3'
Const.TXT_NUM = '4'

Const.M4A = 'm4a'
Const.MP4 = 'mp4'
Const.JPG = 'jpg'
Const.TXT = 'txt'


Const.DICT = {Const.MP4_NUM: Const.MP4,
              Const.M4A_NUM: Const.M4A,
              Const.JPG_NUM: Const.JPG,
              Const.TXT_NUM: Const.TXT}
print(Const.DICT['1'])
