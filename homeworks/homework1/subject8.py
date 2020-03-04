# -*- encoding: utf-8 -*-
"""
@File : subject8,
@Time : 2020/3/4 21:13
@Author : lryself
@Version : 1.0
@Contact : lnolvwe@163.com
"""
"""
题目：设计一个数据结构，用来存放10个员工的信息并初始化，每个员工信息包括：工号，姓名，工龄，工资； 将这10个员工，按照工资从高到低打印输出；
"""
# here put the import lib




import random
class Staff:
    def __init__(self, a, b, c, d):
        self.id = a
        self.name = b
        self.age = c
        self.price = d

    def put(self):
        print(
            "工号：",
            self.id,
            "姓名：",
            self.name,
            "工龄：",
            self.age,
            "工资：",
            self.price)
        return ""


staffs = []
for i in range(10):
    a = 202001 + i
    b = "Staff" + str(random.randint(1000, 9999))
    c = random.randint(25, 60)
    d = random.randint(5000, 10000)
    staffs.append(Staff(a, b, c, d))

for i in sorted(staffs, key=lambda staff: staff.price, reverse=True):
    print(i.put(), end="")
