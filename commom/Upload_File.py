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
import time
from commom.Logs import Log

# 调用日志模块
log = Log(__name__)
logger = log.Logger


class Upload_File(object):
    """
    封装upload方法
    """

    def __init__(self, url, headers, qaz, params=None, data=None, files=None, **kwargs):
        """
        :param url: 请求地址
        :param headers: 请求头
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
        self.header = headers
        self.data = data
        self.qaz = qaz
        self.files = files
        self.params = params

    def upload(self):
        if self.qaz == '3':
            try:
                res = self.__upload_image()
            except Exception as result:
                print(result)
                logger.error(f'{result}')
            else:
                logger.info('image上传完成')
                return res
        elif self.qaz == '1':
            try:
                res = self.__upload_m4a()
            except Exception as result:
                print(result)
                logger.error(f'{result}')
            else:
                logger.info('m4a上传完成')
                return res
        else:
            print('待补充')

    # 外部只暴露upload方法，其他为私有方法
    def __upload_image(self):
        params = {'qaz': 3,
                  'client_timestamp': int(time.time())}
        res = requests.post(url=self.url, headers=self.header, data=self.data, files=self.files, verify=False, params=params)
        return res.json()

    def __upload_m4a(self):
        params = {'qaz': 1,
                  'client_timestamp': int(time.time())}
        res = requests.post(url=self.url, headers=self.header, files=self.files, verify=False, params=params)
        return res.json()


if __name__ == '__main__':
    # 多个文件时使用字典或者数组即可，字段代表含义：
    # '文件1：part:'('文件名称:file_name',  '文件值：value', '文件类型：content_type')
    url = "http://test.api.pokekara.com/api/common/upload_file"
    header = {'Cookie': 'poke_session_id'
                    '=MTYwODYzMDg5NHxjOUd0Z1ZiVHpOX3hoNGxMZUlXSmlINEwyX2lXZmlhS0V0WVZMNUM2UXZzVTczTlBfVDlzU1hWRHdKVkFIaFlhbTdHWUJKZmUyc0k2cEtnUElqTC1tZzlzWklFR1ZzTFF8GiwvPYq-_QjikjO6kO9Op5uvJLJ-qvmQOcY0nq2eka0=;',
          'Host': 'test.api.pokekara.com',
          'Content-Length': '1415663'}

    # 上传image
    # file_path = "E:/pokeinterface/datas/file/image/avater_image/_MG_2818.jpg"
    # params = {'qaz': 3}
    # with open(file_path, 'rb') as f:
    #     files = {
    #         'file': ('_MG_2818.jpg',  f.read(), 'multipart/form-data'),
    #         'filetype': ('', 'jpg', 'multipart/form-data; charset=utf-8')}
    # res = Upload_File(url=url, headers=header, qaz='3', files=files).upload()
    # print(res)

    # 上传m4a
    music_path = 'E:/pokeinterface/datas/file/music/song_record/song_record.m4a'
    params_music = {'qaz': 1}
    with open(music_path, 'rb') as f:
        files_music = {
            'file': ('1608717653.m4a', f.read(), 'application/octet-stream'),
            'filetype': ('', 'm4a', 'multipart/form-data; charset=utf-8')
        }
    music_res = Upload_File(url=url, headers=header, qaz='1', files=files_music).upload()
    print(music_res)