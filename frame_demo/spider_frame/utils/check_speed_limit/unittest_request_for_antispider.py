# -*- coding:utf-8 -*-
# @Time : 2020/9/11 20:51
# @Author : liruiyang
# @File : unittest_request_for _antispider
# @Software: PyCharm
# 使用说明：将Request类的setUp方法中设置你需要设置的内容，生成的测试报告在result_report文件夹中。
# 使用说明：不要使用pycharm默认的pytest运行！！！
import random
import unittest
from BeautifulReport import BeautifulReport
import requests
from requests.adapters import HTTPAdapter
from ...configs import config,read_resource


proxy_pool = config.PORXY_POOL_URL


def get_proxy_ip() -> dict:
    requests.adapters.DEFAULT_RETRIES = 5
    requests_session = requests.session()
    requests_session.mount('http://', HTTPAdapter(max_retries=5))
    requests_session.keep_alive = False
    try:
        proxy = requests_session.get(proxy_pool).text
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


class RequestTest(unittest.TestCase):
    def setUp(self) -> None:
        self.test_url = "https://zcy.86links.com/"
        self.headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate, compress',
            'Accept-Language': 'en-us;q=0.5,en;q=0.3',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'User-Agent': random.choice(read_resource.get_useragent()),
            "Cookie": random.choice(read_resource.get_cookie())
        }

    def test_request(self):
        '''
        单元测试，请求网页
        :param test_url:需要测试的目标网址
        :return:
        '''
        requests_session = requests.session()
        requests_session.mount('http://', HTTPAdapter(max_retries=5))
        requests_session.keep_alive = False
        response = requests_session.get(self.test_url, headers=self.headers)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    suite = unittest.TestSuite()

    # 测试次数及需要测试的模块
    for i in range(100):
        suite.addTest(RequestTest('test_request'))

    # 实例化BeautifulReport模块(用于生成测试模板)
    run = BeautifulReport(suite)

    # 测试名（不可为空）
    test_name = 'test_request'

    run.report(filename='result_report\\'+test_name, description=test_name + '测试结果')