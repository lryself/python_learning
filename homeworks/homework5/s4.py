# -*- encoding: utf-8 -*-
'''
@File : s4.py
@Time : 2020/04/06 18:49:30
@Author : lryself 
@Version : 1.0
@Contact : lnolvwe@163.com
题目：
    编写装饰器来实现，对目标函数进行装饰，分3种情况：目标函数无参数无返回值，目标函数有参数，目标函数有返回值；
     三个目标函数分别为：
     A 打印输出20000之内的素数；
     B 计算整数2-10000之间的素数的个数；
     C 计算整数2-M之间的素数的个数；
'''
import datetime
from functools import wraps
# here put the import lib
def runtime(func):
    @wraps(func)
    def wrapper(*args):
        a=datetime.datetime.now()
        res=func(*args)
        b=datetime.datetime.now()
        print(func.__name__,"函数运行时间为：",b-a)
        return res
    return wrapper

@runtime
def printprime():
    for i in range(2,20000):
        for j in range(2,i):
            if i%j==0 :
                break
        else:
            print(i)

@runtime
def countprime1():
    num=0
    for i in range(2,20000):
        for j in range(2,i):
            if i%j==0 :
                break
        else:
            num+=1
    return num

@runtime
def countprime2(a):
    num=0
    for i in range(2,a):
        for j in range(2,i):
            if i%j==0 :
                break
        else:
            num+=1
    return num

printprime()
print(countprime1())
print(countprime2(10000))