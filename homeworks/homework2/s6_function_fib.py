# -*- encoding: utf-8 -*-
"""
@File : s6_function_fib
@Time : 2020/3/8 17:18
@Author : lryself
@Version : 1.0
@Contact : lnolvwe@163.com
"""
"""
题目：定义一个函数, 打印输出n以内的斐波那契数列;
"""


# here put the import lib
def fib(a, b, c):
  print(a,end=" ")
  if b < c:
    fib(b, a + b, c)


n = int(input("请输入一个数："))
fib(0, 1, n)
