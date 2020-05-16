# -*- encoding: utf-8 -*-
"""
@File : s1
@Time : 2020/5/7 19:43
@Author : lryself
@Version : 1.0
@Contact : lnolvwe@163.com
题目：通过网址 [https://www.tianyancha.com]:随便输入一个企业的名称，得到这个企业的网址
"""
from bs4 import BeautifulSoup
import requests
import os
from tools import cur_file_dir
# here put the import lib
os.chdir(cur_file_dir())

print("注意：运行前请获取你的cookies并复制到cookies.txt中,否则，程序会运行失败")
with open("cookies.txt", "r", encoding="utf-8") as f:
    cookies = f.read()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
    'Cookie': cookies
}
company_name = input("请输入公司名称：")
# company_name = '当当'  # 测试搜索公司
# 伪装为浏览器
# 请求网址

url_list = []
page_num = int(input("请输入你要爬取的页数"))
# page_num=3
print("开始爬取")
for p in range(1, page_num):
    url = 'https://www.tianyancha.com/search/p{}?key='.format(p) + company_name
    r = requests.get(url, headers=headers).content.decode('utf-8')
    # with open("url.txt","w",encoding="utf-8") as f:
    #     f.write(r)
    # 解析html文档
    soup = BeautifulSoup(r, 'html.parser')  # 这里用lxml会出错
    if soup.find(class_="no-result-right") is not None:
        print("只有{}页搜索结果".format(p - 1))
        break
    # 查找每个练习的a链接href属性获取对应的链接地址
    re_a = soup.find(
        id="web-content").find_all(class_="search-item sv-search-company")
    for i in re_a:
        for j in i.find_all("a"):
            try:
                if j.attrs["tyc-event-ch"] == "CompanySearch.Company":
                    url_list.append(j.attrs["href"])
            except Exception:
                pass

# 从url_list中爬取每个网页的网址，存入res中
answers = []
w = 0
for i in url_list:
    test = requests.get(i, headers=headers).content.decode('utf-8')
    soup_test = BeautifulSoup(test, "html.parser")

    if soup_test.find('head').text == '404 Not Found':
        print(x + "打开失败")
        continue

    res = soup_test.find(class_="company-link")
    if res is not None:
        w += 1
        print("已爬取{}条".format(w))
        answers.append(res.attrs["href"] + "\n")
try:
    with open("url.txt", "w", encoding="utf-8"):
        pass
    with open("url.txt", "a", encoding="utf-8") as f:
        for i in set(answers):
            f.write(i)
except Exception as e:
    print(e)
    for i in set(answers):
        print(i)

print("爬取完成")
