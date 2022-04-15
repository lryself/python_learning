# -*- encoding: utf-8 -*-
"""
@File : s10_function_cacluate
@Time : 2020/3/8 17:58
@Author : lryself
@Version : 1.0
@Contact : lnolvwe@163.com
题目：编写一个函数cacluate, 可以实现2个数的运算(加,减 乘,除)
"""
import re
# here put the import lib


def cacluate(a, b, c="+"):
    if c == "+":
        return a + b
    elif c == "-":
        return a - b
    elif c == "*":
        return a * b
    elif c == "/":
        if b != 0:
            return a / b
        else:
            return None


data1 = input("请输入一个算式：（加减乘除）")
data2 = re.findall(r'\d+', data1)
data3 = data1[data1.find(data2[0]) + len(data2[0])]
print(cacluate(int(data2[0]), int(data2[1]), data3))
