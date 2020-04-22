# -*- encoding: utf-8 -*-
"""
@File : s8_struct
@Time : 2020/3/4 21:13
@Author : lryself
@Version : 1.0
@Contact : lnolvwe@163.com
"""
"""
题目：设计一个数据结构，用来存放10个员工的信息并初始化，每个员工信息包括：工号，姓名，工龄，工资； 将这10个员工，按照工资从高到低打印输出；
"""
import random
import tools
# here put the import lib
staffs = []
for i in range(10):
    staff={}
    staff["工号"] = 202001 + i
    staff["姓名"] = tools.random_name()
    staff["年龄"] = random.randint(25, 60)
    staff["工资"] = random.randint(5000, 10000)
    staffs.append(staff)

for i in sorted(staffs, key=lambda staff: staff["工资"], reverse=True):
    print(i)
