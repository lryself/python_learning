# -*- encoding: utf-8 -*-
'''
@File : s3_password.py
@Time : 2020/03/26 22:52:53
@Author : lryself 
@Version : 1.0
@Contact : lnolvwe@163.com
题目：从键盘输入5个同学的账号和密码,然后将他们的姓名,账号和密码(密码需要加密)保存到一个文件中;
'''
import hashlib
import random
import os
import tools
# here put the import lib
data1=[]
for i in range(5):
    a,b,c=input("请输入第{}个同学的姓名，账号和密码，用空格隔开:".format(i+1)).split(" ")
    # a=tools.random_name()
    # b=random.randint(10000000,20000000)
    # c=random.randint(100000,999999)
    data1.append((a,b,c))
print(data1)
with open("user.txt", "w", encoding="utf-8") as f:
    for i in data1:
        md5=hashlib.md5()
        md5.update(str(i[2]).encode("utf-8"))
        f.write("{},{},{}\n".format(i[0],i[1],md5.hexdigest()))
print("加密储存完成！")