# -*- encoding: utf-8 -*-
'''
@File : 练习五.py
@Time : 2020/03/04 09:25:01
@Author : lryself 
@Version : 1.0
@Contact : lryself@163.com
'''

# here put the import lib
'''题目：找质数
'''
for a in range(30, 40):
    for x in range(2, a):
        if (a % x == 0):
            print(a, "=", x, "*", a // x)
            print(a, "不是质数")
    else:
        print(a, "是质数")
