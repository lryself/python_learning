# -*- encoding: utf-8 -*-
"""
@File : practice3
@Time : 2020/3/6 9:45
@Author : lryself
@Version : 1.0
@Contact : lnolvwe@163.com
"""
"""
题目：初始化一个列表(1-20之间的整数) ; 然后 使用匿名函数,列表解析式, 来打印输出一个列表中的奇数;
"""
import random
# here put the import lib
data1=[random.randint(1,20) for x in range(20)]
avs=filter(lambda x:x%2==1,data1)
print(list(avs))