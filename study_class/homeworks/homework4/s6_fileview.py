# -*- encoding: utf-8 -*-
'''
@File : s6_fileview.py
@Time : 2020/03/27 18:34:59
@Author : lryself 
@Version : 1.0
@Contact : lnolvwe@163.com
题目：通过Python来实现显示给定文件夹下的所有文件和文件夹,以及时间，如果是文件，显示大小; 输出格式效果如下:
    名称         日期                   类型（文件夹或者 文件）       大小
'''
import os
import datetime
# here put the import lib
file1=input("请给定一个文件夹：(绝对路径)")
# file1="F:\programme\GitHub\python_learning\homeworks\homework4"



print("{0:28} {1:28} {2:12} {3:10}".format("名称","日期","类型","大小"))
list1=os.listdir(file1)
for i in list1:
    i=os.path.join(file1,i)
    data=[]
    data.append(os.path.basename(i))
    data.append(datetime.datetime.fromtimestamp(os.path.getmtime(i)))
    data.append(os.path.getsize(i))
        
    if os.path.isfile(i):
        print("{0:30} {1:30} {2:5} {3:10d}kb".format(data[0],data[1].strftime('%Y/%b/%d %H:%M:%S'),"文件",data[2]))
    if os.path.isdir(i):
        print("{0:30} {1:30} {2:5}".format(data[0],data[1].strftime('%Y/%b/%d %H:%M:%S'),"文件夹"))