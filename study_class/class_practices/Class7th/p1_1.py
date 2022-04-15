# -*- encoding: utf-8 -*-
'''
@File : p1_1.py
@Time : 2020/03/11 10:14:00
@Author : lryself 
@Version : 1.0
@Contact : lnolvwe@163.com
题目：
'''


# here put the import lib
def fib(a, b, c):
    print(a, end=" ")
    if b < c:
        fib(b, a + b, c)


if __name__ == "__main__":
    fib(0, 1, 100)
