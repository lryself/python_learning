# -*- encoding: utf-8 -*-
'''
@File : s2_os_write&read.py
@Time : 2020/03/18 09:07:08
@Author : lryself 
@Version : 1.0
@Contact : lnolvwe@163.com
题目：同级文件夹里面打开;  同级目录下的子目录里面打开; 上一级文件目录中的其他文件夹中打开,构造上述文件结构,分别在指定位置打开文件进行写入操作;
'''
import os
# here put the import lib

os.chdir("F:\编程\GitHub\python_learning\practices\Class 9th\os_practice")
path1=os.getcwd()
f = open(path1+'\\run1.txt', 'w')
f.write("hallo python 1")
f.close
with open("a_file\\bb.txt","w") as f:
    f.write("hallo python 2")