# -*- encoding: utf-8 -*-
"""
@File : s7_for
@Time : 2020/3/4 21:01
@Author : lryself
@Version : 1.0
@Contact : lnolvwe@163.com
"""
"""
题目：打印输出9*9乘法表
"""
# here put the import lib
for i in range(1,10):
  for j in range(1,i+1):
    print(j,"*",i,"=",j*i,end="  ")
  else:
    print("")
