# -*- encoding: utf-8 -*-
'''
@File : s2_web_re.py
@Time : 2020/04/19 10:26:38
@Author : lryself 
@Version : 1.0
@Contact : lnolvwe@163.com
题目：给定100个企业网站首页链接地址（用1中给出的URL地址）；请爬取每个页面上，企业介绍的链接地址；
    说明，满足企业介绍网址的条件是， 标题包含：企业介绍，关于我们，企业发展，发展历史，企业概况等关键字的URL地址；
    提示：要用到requests库，BeautifulSoup库
'''
import requests
import re
import os
import homeworks.homework7.s2_web_re.tools
import urllib
from bs4 import BeautifulSoup
# here put the import lib
with open("webspiderurl.txt", "r", encoding="utf-8") as f1:
    with open("answer.txt", "w", encoding="utf-8") as f2:
        for i in f1:
            url=i.strip()
            try:
                print("正在链接网址{}".format(url))
                headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
                response = requests.get(url,headers=headers,timeout=5).content.decode('utf-8')
            except:
                print("{}链接失败".format(url))
            else:
                soup=BeautifulSoup(response,'html.parser')
                list1=soup.find_all("a")
                answer=set()
                for i in list1:
                    if re.search("(((企业)|(公司))介绍)|(关于我们)|(((企业)|(公司))发展)|(发展历史)|(((企业)|(公司))概况)|(走进.*)",i.text):
                        answer.add(url.rstrip('/')+'/'+i.attrs['href'].lstrip('/')+"\n")
                for i in answer:
                    f2.write(i)