# -*- encoding: utf-8 -*-
"""
@File : s5_random
@Time : 2020/3/4 19:54
@Author : lryself
@Version : 1.0
@Contact : lnolvwe@163.com
"""
'''题目：使用random模块，生成随机数，来初始化一个列表，元组；
'''

import random
# here put the import lib
num1 = []
num2 = (random.randint(10, 40))
for i in range(10):
    num1.append(random.randint(0, 20))
print(num1)
print(num2)
