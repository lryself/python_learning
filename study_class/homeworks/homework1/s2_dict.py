# -*- encoding: utf-8 -*-
"""
@File : s2_dict
@Time : 2020/03/04 17:30:23
@Author : lryself
@Version : 1.0
@Contact : lnolvwe@163.com
"""
'''题目：一个字典中，存放了10个学生的学号（key）和分数（value）；请筛选输出，大于80分的同学（按照格式：学号：分数）；
'''
import random
# here put the import lib
stus={}
for i in range(202000, 202010):
    stus[i]=random.randint(60, 100)
print("现有学生：")
print(stus)
print("大于80分的同学有：")
for key, value in stus.items():
    if value>=80:
        print("{}:{}".format(key,value))
