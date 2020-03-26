# -*- encoding: utf-8 -*-
'''
@File : s3_password.py
@Time : 2020/03/26 22:52:53
@Author : lryself 
@Version : 1.0
@Contact : lnolvwe@163.com
题目：从键盘输入5个同学的账号和密码,然后将他们的姓名,账号和密码(密码需要加密)保存到一个文件中;
'''
import base64
import random
import os
from tools import *
# here put the import lib
data1=[]
for _ in range(5):
    # a,b,c=input("请输入第{}个同学的姓名，账号和密码，用空格隔开").split(" ")
    a=random_name()
    b=random.randint(10000000,20000000)
    c=random.randint(000000,999999)
    data1.append((a,b,c))

os.chdir(cur_file_dir())
with open("user.txt","w",encoding="utf-8") as f:
    for i in data1:
        f.write("{},{},{}\n".format(i[0],i[1],base64.b64encode(str(i[2]).encode("utf-8"))))
print("加密储存完成！")