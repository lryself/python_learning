# -*- encoding: utf-8 -*-
'''
@File : s8_test_make.py
@Time : 2020/03/27 19:40:23
@Author : lryself 
@Version : 1.0
@Contact : lnolvwe@163.com
题目：1)生成一个大文件ip.txt,要求1200行，每行随机为172.25.254.1---172.25.254.254之间的一个ip地址;
'''
import tools
from random import randint
# here put the import lib
with open("ip.txt","w",encoding="utf-8") as f:
    for i in range(1200):
        f.write("172.25.254."+str(randint(1,254))+"\n")
print("生成完成！")