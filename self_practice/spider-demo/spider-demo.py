# -*- encoding: utf-8 -*-
"""
@File : spider-demo
@Time : 2020/6/23 22:58
@Author : lryself
@Version : 1.0
@Contact : lnolvwe@163.com
"""
import requests
from lxml import etree
# here put the import lib

def get_img_dict(response):
    all_img = response.xpath('//img')
    all_dict = []
    for i in all_img:
        try:
            img_dict = {"src": i.attrib['src'], "alt": i.attrib['alt']}
            all_dict.append(img_dict)
        except:
            pass
    return all_dict


def test_get_img_dict():
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


if __name__ == '__main__':
    r = requests.get('https://www.baidu.com/link?url=L3jG4AXayvdSfuejocKrmM_7BcCILFzie7d_xKNWJHi&amp;wd=&amp;eqid=8941e361001221ad000000035f06e77d',
                     allow_redirects = False)
    if r.status_code == 302:
        try:
            print(r.headers['location'])
        except:
            print("失败")
    else:
        print("失败")