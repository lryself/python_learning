# -*- encoding: utf-8 -*-
'''
@File : s1_deque.py
@Time : 2020/03/26 09:59:34
@Author : lryself 
@Version : 1.0
@Contact : lnolvwe@163.com
题目：
定义一个10个元素的列表，通过列表自带的函数，实现元素在尾部插入和头部插入并记录程序运行的时间；用deque来实现，同样记录程序所耗费的时间；输出这2个时间的差值；
    提示：列表原生的函数实现头部插入数据：list.insert(0, v)；list.append（2）)
'''
from random import randint
from datetime import *
from collections import deque
# here put the import lib
# data1=[1 for _ in range(10)]
# begintime1=datetime.now().timestamp()#列表头部插入记录时间
# data1.insert(0,0)
# endtime1=datetime.now().timestamp()

# begintime2=datetime.now().timestamp()#列表尾部插入记录时间
# data1.append(0)
# endtime2=datetime.now().timestamp()

# data2=deque(data1)

# begintime3=datetime.now().timestamp()#deque头部插入记录时间
# data2.append(0)
# endtime3=datetime.now().timestamp()

# begintime4=datetime.now().timestamp()#deque头部插入记录时间
# data2.appendleft(0)
# endtime4=datetime.now().timestamp()

# print("列表的insert操作耗时：",endtime1-begintime1)
# print("列表的append操作耗时：",endtime2-begintime2)
# print("deque的append操作耗时：",endtime3-begintime3)
# print("deque的appendleft操作耗时：",endtime4-begintime4)

#方法二
def counttime(func):
    def counttime1(*arg):
        begintime=datetime.now().timestamp()#deque头部插入记录时间
        func(*arg)
        endtime=datetime.now().timestamp()
        return endtime-begintime
    return counttime1

@counttime
def insert1(data,a=0,b=0):
    data.insert(a,b)

@counttime
def append1(data,a=0):
    data.append(0)

@counttime
def insert2(data,a=0):
    data.append(0)

@counttime
def append2(data,a=0):
    data.appendleft(a)

data1=[1 for _ in range(10000000)]
data2=deque(data1)
print("列表的insert操作耗时：",insert1(data1,0,0))
print("列表的append操作耗时：",append1(data1,0))
print("deque的append操作耗时：",insert2(data2,0))
print("deque的appendleft操作耗时：",append2(data2,0))