# -*- encoding: utf-8 -*-
'''
@File : s5_pickle.py
@Time : 2020/03/18 10:29:46
@Author : lryself 
@Version : 1.0
@Contact : lnolvwe@163.com
题目：
练习:
  给定一个字典,保存了5个同学的学号,姓名,年龄;使用pickle模块将数据对象保存到文件中去;
'''
import pickle
import random
import tools
from tools import random_name
# here put the import lib
stulist=[]
for _ in range(5):
    student={"id":random.randint(10000,10005),"name":random_name(),"age":random.randint(18,22)}
    stulist.append(student)
print("原列表",stulist)
with open("s5.txt","wb") as f:
    pickle.dump(stulist,f)
with open("s5.txt","rb") as f:
    stulist2=pickle.load(f)
    print("读取的列表：",stulist2)