# -*- encoding: utf-8 -*-
'''
@File : p2_log.py
@Time : 2020/04/03 09:42:57
@Author : lryself 
@Version : 1.0
@Contact : lnolvwe@163.com
题目：义一个函数, 做2个数的加法;  然后我们定义一个装饰器, 对原函数记录运行日志;
'''
import logging
# here put the import lib

def write_log1(s1):
    def write_log2(*arg):
        logging.warning("执行了加法")
        res=s1(arg[0],arg[1])
        return res
    return write_log2

@write_log1
def addition(a,b):
    return a+b

print(addition(1,2))