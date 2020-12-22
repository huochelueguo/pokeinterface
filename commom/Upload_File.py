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
from requests_toolbelt import MultipartEncoder

# class Upload_File(object):
#
#     def __init__(self, url, header,  qaz, data=None, files=None):
#         # self.file_path = file_path
#         # self.file_type = file_type
#         self.url = url
#         self.header = header
#         self.data = data
#         self.qaz = qaz
#         self.files = files
#
#     def upload_image(self):
#
#         res = requests.post(url=self.url, headers=self.header, data=self.data,files=self.files)
#         print(res)


if __name__ == '__main__':
    file_type = 'jpg'
    file_path = "E:/pokeinterface/datas/file/image/avater_image/_MG_2818.jpg"
    url = "http://test.api.pokekara.com/api/common/upload_file"
    header = {'Cookie': 'poke_session_id=MTYwODYzMDg5NHxjOUd0Z1ZiVHpOX3hoNGxMZUlXSmlINEwyX2lXZmlhS0V0WVZMNUM2UXZzVTczTlBfVDlzU1hWRHdKVkFIaFlhbTdHWUJKZmUyc0k2cEtnUElqTC1tZzlzWklFR1ZzTFF8GiwvPYq-_QjikjO6kO9Op5uvJLJ-qvmQOcY0nq2eka0=;',

              'Host':'test.api.pokekara.com',
              'Content-Length':'1415663'}

    # files=[('file',('_MG_2818.jpg',open(file_path,'rb'),'image/jpeg'))]
    files = {
        'file': ('_MG_2818.jpg',  # 文件名称
                      open(file_path,'rb'), 'image/jpeg'), # 文件路径'image/jpeg',  # 文件类型
                'filetype': 'jpg'}

    # payload={'filetype': 'jpg'}
    # m = MultipartEncoder(
    #     fields={'filetype': 'jpg',
    #             'file': ('_MG_2818.jpg', open(file_path, 'rb'), 'image/jpeg')}
    # )
    #
    # r = requests.post(url=url, data=m,
    #               headers=header)
    response = requests.request("POST", url, headers=header,  files=files)
    print(files)
# import requests
#
# url = "http://test.api.pokekara.com/api/common/upload_file"
#
# payload={'filetype': 'jpg'}
# files=[
#     ('file',('_MG_2818.jpg',open('F:/Train/TRAIN/_MG_2818.jpg','rb'),'image/jpeg'))
# ]
# headers = {
#     'Cookie': 'poke_session_id=MTYwODYzMDg5NHxjOUd0Z1ZiVHpOX3hoNGxMZUlXSmlINEwyX2lXZmlhS0V0WVZMNUM2UXZzVTczTlBfVDlzU1hWRHdKVkFIaFlhbTdHWUJKZmUyc0k2cEtnUElqTC1tZzlzWklFR1ZzTFF8GiwvPYq-_QjikjO6kO9Op5uvJLJ-qvmQOcY0nq2eka0=;',
#     'Content-Type': 'multipart/form-data; boundary=2280064a-9152-4fc5-8185-a2a4fe0be6fd'
# }
#
# response = requests.request("POST", url, headers=headers, data=payload, files=files)
#
# print(response.text)