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

from commom import Shell
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

    try:
        shell = Shell.Shell()
        cmd = 'allure generate %s -o %s --clean' % ('./report', './report/allure_raw')
        logger.info("开始执行报告生成")
        print("开始执行报告生成")
        shell.invoke(cmd)
        logger.info("报告生成完毕")
        print("报告生成完毕")
    except Exception as e:
        print("报告生成失败，请重新执行", e)
        logger.error("报告生成失败，请重新执行", e)
        # log.error('执行用例失败，请检查环境配置')
        raise