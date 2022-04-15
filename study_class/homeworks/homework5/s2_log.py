# -*- encoding: utf-8 -*-
'''
@File : s2.py
@Time : 2020/04/06 17:19:42
@Author : lryself 
@Version : 1.0
@Contact : lnolvwe@163.com
题目：编写一个装饰器，能记录其他函数调用的日志，将日志写入到文件中
'''
import logging
import tools
from functools import wraps
# here put the import lib

file_hander=logging.FileHandler("s2_logs.log", encoding="utf-8", mode="a")
logging.basicConfig(
    handlers=[file_hander,]
)

def log1(func):
    @wraps(func)
    def log2(*args):
        logging.warning("{}函数被调用了".format(func.__name__))
        res=func(*args)
        return res
    return log2

@log1
def addition(*args):
    sum=0
    for i in args:
        sum+=i
    return sum

print(addition(3,5))