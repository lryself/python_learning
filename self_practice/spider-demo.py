# -*- encoding: utf-8 -*-
"""
@File : spider-demo
@Time : 2020/6/23 22:58
@Author : lryself
@Version : 1.0
@Contact : lnolvwe@163.com
"""
from tools_main import cur_file_dir
import os
os.chdir(cur_file_dir())
import requests
from lxml import etree
# here put the import lib


def get_img_dict(response):
    all_img = response.xpath('//img')
    all_dict=[]
    for i in all_img:
        try:
            img_dict = {"src": i.attrib['src'], "alt": i.attrib['alt']}
            all_dict.append(img_dict)
        except:
            pass
    return all_dict


if __name__ == '__main__':
    url = 'http://www.comtrans.com.cn/about/honor.html'
    try:
        print("正在链接网址{}".format(url))
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
        response = etree.HTML(requests.get(url, headers=headers, timeout=5).content.decode("utf-8"))
    except:
        print("{}链接失败".format(url))
    else:
        for i in get_img_dict(response):
            print(i)
