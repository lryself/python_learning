# -*- encoding: utf-8 -*-
'''
@File : s3_multiprocessing.py
@Time : 2020/04/24 19:36:40
@Author : lryself 
@Version : 1.0
@Contact : lnolvwe@163.com
题目：计算1～100000之间所有素数的个数， 要求如下:
- 编写函数判断一个数字是否为素数，然后统计素数的个数；
-对比1: 对比使用多进程和不使用多进程两种方法的统计速度。
-对比2：对比开启4个多进程和开启10个多进程两种方法的速度。
'''
from multiprocessing import Process,Queue,Pool
import time
# here put the import lib
def isprime(n):
    if n>=2:
        for i in range(2,n):
            if n%i==0:
                break
        else:
            return True
    return False

def count_time(func):
    def count_time1(*args):
        start=time.time()
        res=func(*args)
        end=time.time()
        print(end-start)
        return res
    return count_time1

@count_time
def processes(n):
    po=Pool(n)
    res=po.map_async(func=isprime,iterable=range(1,100000))
    po.close()
    po.join()
    count=0
    for i in res._value:
        if i==True:
            count+=1
    return count

@count_time
def one_process():
    count=0
    for i in range(1,100000):
        if isprime(i):
            count+=1
    return count

if __name__ == "__main__":
    print("不使用多进程的用时：",end="")
    print("1 进程结果："+str(one_process()))
    print("使用4个进程的用时：",end="")
    print("4 进程结果："+str(processes(4)))
    print("使用10个进程的用时：",end="")
    print("10 进程结果："+str(processes(10)))