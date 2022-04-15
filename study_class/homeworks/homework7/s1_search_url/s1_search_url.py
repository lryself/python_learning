# -*- encoding: utf-8 -*-
'''
@File : s1_search_url.py
@Time : 2020/04/18 10:20:07
@Author : lryself 
@Version : 1.0
@Contact : lnolvwe@163.com
题目：给定一个文件，请用正则表达式，逐行匹配提取其中的URL链接信息，并保存到另外一个文件中；
   提示，文件有1000行，注意控制每次读取的行数；
'''
import re
import os
import tools
# here put the import lib
with open("s1_webspiderUrl_answer.txt", "w", encoding="utf-8") as f:
    pass
with open("webspiderUrl.txt", "r", encoding="utf-8") as f:
    with open("s1_webspiderUrl_answer.txt", "a", encoding="utf-8") as f1:
        for i in f:
            res=re.findall(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F])|[\u4e00-\u9fa5])+",i)
            for j in res:
                s1=j.split(";")
                for w in s1:
                    w=w.strip(";")
                    w=w.strip(")")
                    w=w.strip("\'")
                    s2=re.search(r"(http[s]?://)?([a-zA-Z]|[0-9]|[$-_@.&+]|[!*,]|[\u4e00-\u9fa5])+",w)
                    if s2:
                        f1.write(s2.group()+"\n")