# -*- encoding: utf-8 -*-
"""
@File : s8_function_stringnum
@Time : 2020/3/8 17:36
@Author : lryself
@Version : 1.0
@Contact : lnolvwe@163.com
题目：定义一个函数，给定一个字符串，找出该字符串中出现次数最多的那个字符，并打印出该字符及其出现的次数。
"""
import operator

# here put the import lib
string = input("请输入一个字符串:")


def findmax(a):
  dict1 = {}
  b = list(a)
  for i in b:
    if dict1.get(i) != None:
      dict1[i] += 1
    else:
      dict1[i] = 1
  return max(dict1.items(), key=operator.itemgetter(1))


data2=findmax(string)
print(data2[0],":",data2[1])
