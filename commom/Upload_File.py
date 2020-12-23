# # !usr/bin/env python
# # -*- coding:utf-8 _*-
# """
# @Author:孙泽
# @Github:https://github.com/huochelueguo
# @File:Upload_File.py
# @Time:NAME.py@Time:2020/12/22 20:23
# @ 上传文件通用接口
# 参数qaz翻译：
#     1： m4a
#     2:  mp4
#     3:  jpg
#     4:  txt
# """
import requests


class Upload_File(object):

    def __init__(self, url, header, qaz, data=None, files=None):
        self.url = url
        self.header = header
        self.data = data
        self.qaz = qaz
        self.files = files

    def upload(self):
        if self.qaz == '3':
            return self.upload_image()

    def upload_image(self):
        res = requests.post(url=self.url, headers=self.header, data=self.data, files=self.files)
        return res.json()


if __name__ == '__main__':
    file_path = "/Users/sunwenxiao/Desktop/_MG_2135-1.jpg"
    url = "http://test.api.pokekara.com/api/common/upload_file"
    header = {'Cookie': 'poke_session_id=MTYwODYzMDg5NHxjOUd0Z1ZiVHpOX3hoNGxMZUlXSmlINEwyX2lXZmlhS0V0WVZMNUM2UXZzVTczTlBfVDlzU1hWRHdKVkFIaFlhbTdHWUJKZmUyc0k2cEtnUElqTC1tZzlzWklFR1ZzTFF8GiwvPYq-_QjikjO6kO9Op5uvJLJ-qvmQOcY0nq2eka0=;',
              'Content_Type':'multipart/form-data'}
    files = {'file': ('_MG_2818.jpg',  # 文件名称
                    open(file_path,'rb'), 'image/jpeg'), # 文件路径'image/jpeg',  # 文件类型
                    'filetype': 'jpg'
             }
    data = {'qaz': '3'}
    res = Upload_File(url=url, header=header, qaz='3', data=data, files=files).upload_image()
    print(res)