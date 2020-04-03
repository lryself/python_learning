# -*- encoding: utf-8 -*-
'''
@File : p1_counter.py
@Time : 2020/04/03 08:39:11
@Author : lryself 
@Version : 1.0
@Contact : lnolvwe@163.com
题目：利用闭包返回一个计数器函数，每次调用它返回递增整数：
'''

# here put the import lib
def createCounter():
    x=0
    def c1():
        nonlocal x
        x+=1
        return x
    return c1

counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')