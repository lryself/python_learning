# -*- encoding: utf-8 -*-
"""
@File : s1
@Time : 2020/3/8 15:54
@Author : lryself
@Version : 1.0
@Contact : lnolvwe@163.com
"""
"""
题目：写函数，判断用户传入的对象（字符串、列表、元组）长度,并返回给调用者。
"""

# here put the import lib


def judge_len(a):
    return len(a)


data1 = "Hallo Python"
data2 = ("h1", "h2", "h3")
data3 = ["b1", "b2", "b3", "b4"]
print(judge_len(data1))
print(judge_len(data2))
print(judge_len(data3))
