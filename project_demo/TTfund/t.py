# coding: utf-8
# @Author : lryself
# @Date : 2021/8/5 22:51
# @Software: PyCharm
from time import sleep

import requests
from selenium import webdriver


def get_selenium_html(path, url) -> int:
    option = webdriver.ChromeOptions()
    option.add_argument('headless')

    # browser = webdriver.Chrome(executable_path=path, options=option)
    browser = webdriver.Chrome(executable_path=path)
    # 进入无头模式更换上列代码
    p = 0
    try:
        browser.get(url)
        p = browser.find_element_by_xpath('//*[@id="pagebar"]/label[7]').text
    except Exception as e:
        print(e)
    finally:
        browser.close()
        return p


if __name__ == '__main__':
    pages = get_selenium_html(path='D:\software\chromedriver.exe', url="http://fund.eastmoney.com/data/fundranking.html")
    print(pages)
