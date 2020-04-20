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
import tools
import urllib
# here put the import lib
with open("webspiderurl.txt","r",encoding="utf-8") as f1:
    with open("answer.txt","w",encoding="utf-8") as f2:
        w=1
        for i in f1:
            url=i.strip()
            try:
                print("正在链接第{}个网址".format(w))
                response=requests.get(url,timeout=1)
            except:
                print("第{}个网址链接失败".format(w))
            else:
                f2.write(url+"\n")
            finally:
                w+=1