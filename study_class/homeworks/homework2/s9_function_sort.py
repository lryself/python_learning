# -*- encoding: utf-8 -*-
"""
@File : s9_function_sort
@Time : 2020/3/8 17:53
@Author : lryself
@Version : 1.0
@Contact : lnolvwe@163.com
题目：定义一个函数，函数接收一个数组，并把数组里面的数据从小到大排序
"""
import random


# here put the import lib
def sort1(a):
  a.sort()


data1 = [random.randint(-100, 100) for _ in range(20)]
print("原数组：",data1)
sort1(data1)
print("新数组：",data1)
