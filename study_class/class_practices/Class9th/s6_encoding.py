# -*- encoding: utf-8 -*-
'''
@File : s6_encoding.py
@Time : 2020/03/18 10:31:28
@Author : lryself 
@Version : 1.0
@Contact : lnolvwe@163.com
题目：
练习:  读取文件里面的内容(包含中文), 进行打印输出显示;
         注意:  请设置文件的不同编码格式进行观察;  另外,文件内容中包含中文字符;
'''
import tools
# here put the import lib
f=open("s6.txt", "r", encoding="utf-8")
print("utf-8读取：",f.read())
f=open("s6.txt", "r", encoding="gbk")
print("gbk读取：",f.read())