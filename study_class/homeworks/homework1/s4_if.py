# -*- encoding: utf-8 -*-
"""
@File : s4_if.py
@Time : 2020/03/04 18:10:47
@Author : lryself 
@Version : 1.0
@Contact : lryself@163.com
"""
'''题目：判断用户输入的年份是否为闰年
'''

# here put the import lib
year: int = int(input("请输入一个公元后的年份:"))
if year % 400 == 0:
  print(year, "是闰年")
else:
  if year % 4 == 0 & year % 100 != 0:
    print(year, "是闰年")
  else:
    print(year, "不是闰年")
