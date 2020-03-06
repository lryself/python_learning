# -*- encoding: utf-8 -*-
"""
@File : practice1
@Time : 2020/3/6 8:12
@Author : lryself
@Version : 1.0
@Contact : lnolvwe@163.com
"""
"""
题目：定义一个函数,来计算苹果的价格(重量*价格); 通过键盘输入重量和价格,然后调用函数来计算;
"""


# here put the import lib
def price(a, b):
  return a * b


a, b = input("请输入苹果的单价和重量，用空格隔开").split(" ")
print("苹果的价格是：", price(int(a), int(b)))