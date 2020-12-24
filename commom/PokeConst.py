# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:PokeConst.py
@Time:2020/12/23 下午11:53
"""

from commom import Const
import time

# upload_file类型定义
Const.UPLOAD_FILE_TYPE_M4A_NUM = 1
Const.UPLOAD_FILE_TYPE_MP4_NUM = 2
Const.UPLOAD_FILE_TYPE_JPG_NUM = 3
Const.UPLOAD_FILE_TYPE_TXT_NUM = 4
Const.UPLOAD_FILE_TYPE_M4A = 'm4a'
Const.UPLOAD_FILE_TYPE_MP4 = 'mp4'
Const.UPLOAD_FILE_TYPE_JPG = 'jpg'
Const.UPLOAD_FILE_TYPE_TXT = 'txt'
Const.DICT = {Const.UPLOAD_FILE_TYPE_MP4_NUM: Const.UPLOAD_FILE_TYPE_MP4,
              Const.UPLOAD_FILE_TYPE_M4A_NUM: Const.UPLOAD_FILE_TYPE_M4A,
              Const.UPLOAD_FILE_TYPE_JPG_NUM: Const.UPLOAD_FILE_TYPE_JPG,
              Const.UPLOAD_FILE_TYPE_TXT_NUM: Const.UPLOAD_FILE_TYPE_TXT}

# 时间类型常量
Const.TIMESTAMP_S = int(time.time())
Const.TIMESTAMP_MS = int(round(Const.TIMESTAMP_S * 1000))

print(Const.TIMESTAMP_MS)