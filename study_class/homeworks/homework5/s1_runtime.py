# -*- encoding: utf-8 -*-
'''
@File : s1_runtime.py
@Time : 2020/04/06 16:52:57
@Author : lryself 
@Version : 1.0
@Contact : lnolvwe@163.com
题目：编写一个装饰器，能计算其他函数的运行时间；
'''
import datetime
# here put the import lib

def counttime1(func):
    def counttime12(*args,**arg):
        a=datetime.datetime.now()
        func()
        b=datetime.datetime.now()
        print(b-a)
    return counttime12

@counttime1
def printtime():
    sum=0
    for i in range(10000):
        sum+=i

printtime()