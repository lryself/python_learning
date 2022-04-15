# -*- encoding: utf-8 -*-
"""
@File : s3_function_print
@Time : 2020/3/8 16:10
@Author : lryself
@Version : 1.0
@Contact : lnolvwe@163.com
"""
"""
题目：编写一个函数, 传入一个数字列表, 输出列表中的奇数;
"""
import random
# here put the import lib
def print_Odd(list1):
  for i in list1:
    if i%2==1:
      print(i,end=" ")

data1=[random.randint(1,100) for _ in range(10)]
print("生成的列表是：",data1)
print("其中的奇数是：",end="")
print_Odd(data1)