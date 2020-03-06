# -*- encoding: utf-8 -*-
"""
@File : subject6,
@Time : 2020/3/4 19:43
@Author : lryself
@Version : 1.0
@Contact : lnolvwe@163.com
"""
"""
题目：前面2个元素为0，1，输出100以内的斐波那契数列；
"""
# here put the import lib
fib = [0, 1]
while fib[len(fib) - 1] <= 100:
  fib.append(fib[len(fib) - 1] + fib[len(fib) - 2])
fib.pop()
print(fib)