# -*- encoding: utf-8 -*-
"""
@File : s7_function_level
@Time : 2020/3/8 17:27
@Author : lryself
@Version : 1.0
@Contact : lnolvwe@163.com
"""
"""
题目：
"""
import random


# here put the import lib
def judge(a):
  if a >= 90:
    return "A"
  if 90 > a >= 80:
    return "B"
  if 80 > a >= 70:
    return "C"
  return "D"


stus = [random.randint(60, 100) for _ in range(20)]
print("这20个学生的成绩是：", stus)
print("其对应的等级是：", end="")
for i in stus:
  print(judge(i), end=" ")
