# -*- encoding: utf-8 -*-
"""
@File : s4_function_statistics
@Time : 2020/3/8 16:20
@Author : lryself
@Version : 1.0
@Contact : lnolvwe@163.com
"""
"""
题目：写函数，统计字符串中有几个字母，几个数字，几个空格，几个其他字符，并返回结果;
"""


# here put the import lib
def statistics(a):
  c = [0, 0, 0, 0]
  for i in list(a):
    if i.isdigit():
      c[1] += 1
    elif i == " ":
      c[2] += 1
    elif i.isalpha():
      c[0] += 1
    else:
      c[3] += 1
  return c


str = input("请输入一个字符串:")
data1 = list(str)
data2 = statistics(data1)
print("这个字符串中，有", data2[0], "个字母，有", data2[1], "个数字，有", data2[2], "个空格，有", data2[3], "个其他字符")
