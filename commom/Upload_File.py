# # !usr/bin/env python
# # -*- coding:utf-8 _*-
# """
# @Author:孙泽
# @Github:https://github.com/huochelueguo
# @File:Upload_File.py
# @Time:NAME.py@Time:2020/12/22 20:23
# @ 上传文件通用接口
# 参数qaz翻译：

# """
import requests
from commom.Logs import Log

# 调用日志模块
log = Log(__name__)
logger = log.Logger


class Upload_File(object):
    """
    封装upload方法
    """

    def __init__(self, url, header, qaz, data=None, files=None, **kwargs):
        """
        :param url: 请求地址
        :param header: 请求头
        :param qaz: upload文件类型
                 1： m4a
                 2:  mp4
                 3:  jpg
                 4:  txt
        :param data: 请求数据
        :param files: upload文件
        :param kwargs: 其他requests参数，如params
        """
        self.url = url
        self.header = header
        self.data = data
        self.qaz = qaz
        self.files = files

    def uplaod(self):
        if self.qaz == '3':
            try:
                res = self.__upload_image()
            except Exception as result:
                print(result)
                logger.error(f'{result}')
            else:
                logger.info('image上传完成')
                return res
        else:
            print('待补充')

    # 外部只暴露upload方法，其他为私有方法
    def __upload_image(self):
        """
        :return: 返回response
        """
        res = requests.post(url=self.url, headers=self.header, data=self.data, files=self.files, params=params, verify=False)
        return res.json()


if __name__ == '__main__':

    file_path = "E:/pokeinterface/datas/file/image/avater_image/_MG_2818.jpg"
    url = "http://test.api.pokekara.com/api/common/upload_file"
    header = {'Cookie': 'poke_session_id'
                        '=MTYwODYzMDg5NHxjOUd0Z1ZiVHpOX3hoNGxMZUlXSmlINEwyX2lXZmlhS0V0WVZMNUM2UXZzVTczTlBfVDlzU1hWRHdKVkFIaFlhbTdHWUJKZmUyc0k2cEtnUElqTC1tZzlzWklFR1ZzTFF8GiwvPYq-_QjikjO6kO9Op5uvJLJ-qvmQOcY0nq2eka0=;',
              'Host': 'test.api.pokekara.com',
              'Content-Length': '1415663'}
    params = {'qaz': 3}
    # 多个文件时使用字典或者数组即可，字段代表含义：
    # '文件1：part:'('文件名称:file_name',  '文件值：value', '文件类型：content_type')
    with open(file_path, 'rb') as f:
        files = {
            'file': ('_MG_2818.jpg',  f.read(), 'multipart/form-data'),
            'filetype': ('', 'jpg', 'multipart/form-data; charset=utf-8')}
    res = Upload_File(url=url, header=header, qaz='3', files=files, params=params).uplaod()
    print(res)
