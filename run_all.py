# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:run_all.py
@Time:NAME.py@Time:2020/11/25 18:41
运行主入口
"""
import time
import pytest
from commom.Logs import Log

if __name__ == "__main__":
    # 调用日志模块
    log = Log(__name__)
    logger = log.Logger
    # 默认运行的是当前目录及子目录的所有文件夹的测试用例
    try:
        print("开始执行脚本")
        logger.info("========" + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + "========")
        pytest.main(["-s", "-v"])
        print("脚本执行完成")
    except Exception as e:
        logger.error("脚本批量执行失败！", e)
        print("脚本批量执行失败！", e)

