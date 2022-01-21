# coding: utf-8
# @Author : lryself
# @Date : 2021/6/25 17:32
# @Software: PyCharm
import csv

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import re


def get_html(chrome_path, url, filename):
    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    browser = webdriver.Chrome(executable_path=chrome_path, options=option)

    # browser = webdriver.Chrome(executable_path=chrome_path)
    browser.get(url)
    t1 = browser.find_element_by_xpath("/html/body/table[3]/tbody/tr[2]/td/table/tbody/tr/td/div[3]/div/p[1]")
    t2 = browser.find_element_by_xpath("/html/body/table[3]/tbody/tr[2]/td/table/tbody/tr/td/div[3]/div/p[2]")
    with open(f"../statics/{filename}（文科）.txt", "w", encoding="utf-8") as f:
        f.write(t1.text)
    with open(f"../statics/{filename}（理科）.txt", "w", encoding="utf-8") as f:
        f.write(t2.text)


def spider_school_score(filename):
    with open(f"../statics/{filename}.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
    results = []
    result = {}
    for line in lines:
        if re.match(r"^\[[0-9]{4}\][\u4e00-\u9fa5]+\s*$", line):
            result = {}
            result["学校名称"] = re.findall(r"[\u4e00-\u9fa5]+", line)[0]
        elif re.match(r"^\s*计划数 ：\s*\d+\s*已投数：\s* \d+\s*$", line):
            result["计划数"] = re.findall(r"\d+", line)[0]
        elif re.match(r"^\s*已投考生最低分数 ：\s*\d+.?\d*\s*$", line):
            result["最低分数"] = re.findall(r"\d+.?\d*", line)[0]
            results.append(result)
    return results


def make_data(filename, results: list):
    with open(f"../statics/{filename}", "w", encoding="utf-8", newline='') as f:
        headers = ['学校名称', '计划数', '最低分数']
        f_csv = csv.DictWriter(f, headers)
        f_csv.writeheader()
        f_csv.writerows(results)


if __name__ == '__main__':
    # dic = {
    #     "2020年一本投档线": "https://www.nxjyks.cn/contents/PTGK/2020/08/20200818102928000.html",
    #     "2020年二本投档线": "https://www.nxjyks.cn/contents/PTGK/2020/08/20200824184800000.html",
    #     "2019年一本投档线": "https://www.nxjyks.cn/contents/PTGK/2019/07/20190718085458000.html",
    #     "2019年二本投档线": "https://www.nxjyks.cn/contents/PTGK/2019/07/20190724152031000.html",
    # }
    #
    # for k, v in dic.items():
    #     get_html(
    #         chrome_path="D:\software\chromedriver.exe",
    #         url=v,
    #         filename=k
    #     )
    #     filename = k+"（理科）"
    #     r = spider_school_score(filename)
    #     make_data(f"{filename}.csv", r)
    #     filename = k+"（文科）"
    #     r = spider_school_score(filename)
    #     make_data(f"{filename}.csv", r)
    name = "2021年一本投档线"
    get_html(
        chrome_path="D:\software\chromedriver.exe",
        url="https://www.nxjyks.cn/contents/PTGK/2021/07/20210718111144000.html",
        filename=name
    )
    filename = name+"（理科）"
    r = spider_school_score(filename)
    make_data(f"{filename}.csv", r)
    filename = name+"（文科）"
    r = spider_school_score(filename)
    make_data(f"{filename}.csv", r)
