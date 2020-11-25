# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:孙泽
@Github:https://github.com/huochelueguo
@File:RequestGet.py
@Time:2020/8/21 上午8:56
"""
# 封装get方法

import requests
from commom.Logs import Log

# 调用日志模块
log = Log(__name__)
logger = log.Logger


class Get(object):

    def __init__(self, url, params=None, header=None):
        """
        :param url:
        :param params:
        """
        self.url = url
        self.params = params
        self.header = header

    def get_request(self, **kwargs):
        try:
            if self.url == '':
                print('传入内容为空，请检查')
                logger.error('传入地址为空，请检查')
            else:
                response = requests.get(url=self.url, params=self.params, **kwargs)
                logger.info('get接口返回数据')
                return response.json(), response.status_code
        except TimeoutError:
            logger.error('网络连接超时')
        except Exception as result:
            print(result)
            logger.error(f'{result}')


if __name__ == '__main__':
    url1 = 'http://test.api.pokekara.com/x/artist/simple_info?artist_id=512'
    a = Get(url1).get_request()
    print(a)

