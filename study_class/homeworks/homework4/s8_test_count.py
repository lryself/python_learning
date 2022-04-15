# -*- encoding: utf-8 -*-
'''
@File : s8_test.py
@Time : 2020/03/27 19:39:14
@Author : lryself 
@Version : 1.0
@Contact : lnolvwe@163.com
题目：京东二面笔试题
2)读取ip.txt文件统计这个文件中ip出现频率排前10的ip

'''
import tools
from collections import Counter
# here put the import lib
c=Counter()
try:
    with open("ip.txt", "r", encoding="utf-8") as f:
        for line in f:
            line=line.strip()
            c[line]+=1
except:
    print("未找到ip.txt文件")

d=list(c.items())
d.sort(key=lambda a: a[1],reverse=True)
print("排名前十的ip为：")
for i in range(10):
    print(d[i][0])