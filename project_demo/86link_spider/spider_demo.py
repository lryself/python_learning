# here put the import lib
# @Time : 2020/9/9 12:52
# @Author : liruiyang
# @File : spider_demo
# @Software: PyCharm
from time import sleep

import requests


PORXY_POOL = 'http://115.29.137.201:5000/random'


def get_proxy_ip():
    requests.adapters.DEFAULT_RETRIES = 5
    requests_session = requests.session()
    requests_session.keep_alive = False
    try:
        proxy = requests_session.get(PORXY_POOL).text
    except Exception as e:
        return {
            'code': 500,
            'message': '代理池异常',
            'error': str(e)
        }
    else:
        return {
            'code': 200,
            'message': 'OK',
            'proxy': 'http://{0}'.format(proxy)
        }


def spider_main(url):
    i = 0
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate, compress',
        'Accept-Language': 'en-us;q=0.5,en;q=0.3',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
        "Cookie": '__guid=144548670.3998153801655085000.1599626835610.818; Hm_lvt_c7663d800c04b77c617598afd4f84e0c=1599626837; ZCY86LINKS=98FJGF9AzoRnswFO_cXE6f2s9ex9IbyJrncqDbzjnQGqC9r2zAf9JHTWfADi64w1; monitor_count=31; Hm_lpvt_c7663d800c04b77c617598afd4f84e0c=1599635421'
    }
    while True:
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            return print("访问第{}次出错".format(i))
        i += 1
        print(i)
        if i == 1000:
            return print("成功")


if __name__ == '__main__':
    url = "https://zcy.86links.com/"
    spider_main(url)