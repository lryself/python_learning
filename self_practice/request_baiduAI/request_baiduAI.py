# -*- coding:utf-8 -*-
# @Time : 2020/9/13 15:50
# @Author : liruiyang
# @File : request_baiduAI
# @Software: PyCharm
# @Description: 这是一个python程序
# here put the import lib
import base64

import requests
import tools_main
import os
import json
os.chdir(tools_main.cur_file_dir())


def get_ai_text():
    # request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/handwriting"
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/formula"
    # 二进制方式打开图片文件
    # f = open('test1.jpg', 'rb')
    # f = open('test2.png', 'rb')
    # f = open('test3.png', 'rb')
    f = open('test4.jpg', 'rb')
    img = base64.b64encode(f.read())

    params = {"image": img, "probability": True}
    access_token = '24.212a08cbc00bea695c5cbcd86fd8f87a.2592000.1603364345.282335-22734745'
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        print(response.json())
        with open("test5_result.txt", "w", encoding="utf8") as f:
            f.write(response.text)


def get_token():
    # client_id 为官网获取的AK， client_secret 为官网获取的SK
    # AK = "jejZuQGg8gIP8hkysL0pHrCo"
    # SK = "um4yXKYOtTQETyVANlb2kvIgjEEnQfzd"
    AK = "Z0H3MHuNPhGFvYWpiEMMvWKP"
    SK = "IUGq8MwNI0PXlF9fOU7LAL8SyAClAfQc"
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={AK}&client_secret={SK}'.format(AK=AK, SK=SK)
    response = requests.get(host)
    if response:
        print(response.json())
        with open("token2.txt", "w", encoding="utf8") as f:
            f.write(response.text)


def load_json():
    with open("test5_result.txt", "r", encoding="utf8") as f:
        result = json.loads(f.read())
        print(result)


if __name__ == '__main__':
    # get_token()
    get_ai_text()
    load_json()