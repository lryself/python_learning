#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/13 18:29
# @Author  : kiwanter
# @Email   : kiwanter@163.com
# @File    : status_code_spider.py
# @software: pycharm

'''
@file function:爬取状态码信息
'''

import requests
from lxml import etree

from frame_demo.spider_frame.utils.requests_common import parse_html


def status_code_spider():
    url = 'https://www.runoob.com/http/http-status-codes.html'
    response = requests.get(url)
    html = parse_html(response.text, "html5lib")
    tables = html.find_all("table", class_="reference")
    csv_table = []
    for table in tables:
        for tr in table.find_all("tr"):
            csv_line = []
            for td in tr.find_all("td"):
                csv_line.append(td.text)
            csv_table.append(csv_line) if len(csv_line) > 1 else True
    with open("../../resource/statu_codes.csv", "w", encoding="utf8") as f:
        import csv
        c = csv.writer(f)
        c.writerows(csv_table)


if __name__ == '__main__':
    status_code_spider()