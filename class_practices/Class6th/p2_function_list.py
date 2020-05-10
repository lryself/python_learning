# -*- encoding: utf-8 -*-
"""
@File : practice2
@Time : 2020/3/6 8:25
@Author : lryself
@Version : 1.0
@Contact : lnolvwe@163.com
"""
"""
题目：定义一个函数,  打印输出列表里面的元素;  然后增加列表中的元素, 然后再输出新的列表;  主程序中,打印这个列表的地址(传参之前,传参之后);
"""


# here put the import lib
def printlist(a):
  for i in a:
    print(i, end=" ")
  print()
  a.append(3)
  for i in a:
    print(i, end=" ")
  print()


a = [1, 2, 3, 4, 5, 6, 7, 8]
print(id(a))
printlist(a)
print(id(a))
