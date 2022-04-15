# -*- encoding: utf-8 -*-
'''
@File : s2_os_write&read_2.py
@Time : 2020/03/18 09:23:29
@Author : lryself 
@Version : 1.0
@Contact : lnolvwe@163.com
题目：
'''
import os
# here put the import lib
os.chdir("F:\编程\GitHub\python_learning\practices\Class 9th\os_practice\\a_file")
with open(r"../b_file/a.txt", "r") as f:
    print(f.read())