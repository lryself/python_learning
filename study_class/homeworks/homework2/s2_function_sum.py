# -*- encoding: utf-8 -*-
"""
@File : s2_sum
@Time : 2020/3/8 16:01
@Author : lryself
@Version : 1.0
@Contact : lnolvwe@163.com
"""
"""
题目：编写一个函数,接收n个数字，求这些参数数字的和;
"""

# here put the import lib

def sum_all(l):
    sum = 0
    for i in l:
        sum = sum + i
    return sum


if __name__ == '__main__':
    list1 = input("请输入n个数字，用逗号隔开:").split(",")
    list2 = []
    for i in list1:
        list2.append(int(i))
    print(sum_all(list2))
