# -*- encoding: utf-8 -*-
'''
@File : s7_count_size.py
@Time : 2020/03/27 19:20:01
@Author : lryself 
@Version : 1.0
@Contact : lnolvwe@163.com
题目：使用python代码统计一个文件夹中所有文件的总大小
'''
import os
# here put the import lib
# file1=input("请给定一个文件夹：(绝对路径)")
file1="F:\programme\GitHub\python_learning\homeworks\homework4"
def countsize(f):
    allsize=0
    for i in os.listdir(f):
        i=os.path.join(f,i)
        if os.path.isfile(i):
            allsize+=os.path.getsize(i)
        if os.path.isdir(i):
            allsize+=countsize(i)
    return allsize

print("总大小为：{}".format(countsize(file1)))