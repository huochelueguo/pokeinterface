# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:run_all.py
@Time:NAME.py@Time:2020/11/25 18:41
运行主入口
"""
import pytest

# 默认运行的是当前目录及子目录的所有文件夹的测试用例
pytest.main(["-s", "-v"])