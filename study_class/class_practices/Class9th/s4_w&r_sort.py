# -*- encoding: utf-8 -*-
'''
@File : s4_w&r_sort.py
@Time : 2020/03/18 09:37:13
@Author : lryself 
@Version : 1.0
@Contact : lnolvwe@163.com
题目：
        一个文件内容的如下,请按照行读取文件的内容,  将分数排序后输出到另外一个文件中:
                    姓名      学号      分数
                    张三      101       78
                    李四      102       87
                    王五      103       83
'''
import tools
# here put the import lib
f=open("s3_s4.txt", "r")
list1=f.readlines()
for i in range(len(list1)):
    list1[i]=list1[i].rstrip("\n").split(",")
    list1[i][2]=int(list1[i][2])
list1=sorted(list1,key=lambda li: li[2])
with open("s4.txt", "w") as f:
    for i in list1:
        f.write(i[0]+","+i[1]+","+str(i[2])+"\n")
