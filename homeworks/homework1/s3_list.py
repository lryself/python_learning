# -*- encoding: utf-8 -*-
"""
@File : s3_list.py
@Time : 2020/03/04 18:02:43
@Author : lryself 
@Version : 1.0
@Contact : lryself@163.com
"""
'''题目：定义2个列表，并初始化； 找出这2个列表中，相同的元素并输出；
'''
import random

# here put the import lib
list1 = []
list2 = []
for i in range(10):
  list1.append(random.randint(0, 20))
  list2.append(random.randint(0, 20))
print("两个列表分别是：")
print(list1)
print(list2)
sames = set()
for i in list1:
  for j in list2:
    if i == j:
      sames.add(i)
print("相同的元素有：", sames)
