# -*- encoding: utf-8 -*-
'''
@File : s3_w&r.py
@Time : 2020/03/18 09:33:08
@Author : lryself 
@Version : 1.0
@Contact : lnolvwe@163.com
题目：
        一个文件内容的如下,请读取文件的内容, 并输出;
                    姓名      学号      分数
                    张三      101       78
                    李四      102       87
                    王五      103       83

'''
# here put the import lib
print("姓名         学号        分数")
with open("practices\Class 9th\s3_s4.txt","r") as f:
    for _ in range(3):
        list1=f.readline().split(",")
        print(list1[0],"      ",list1[1],"      ",list1[2],end="")