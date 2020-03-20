# -*- encoding: utf-8 -*-
'''
@File : s3_write_score.py
@Time : 2020/03/20 18:49:30
@Author : lryself 
@Version : 1.0
@Contact : lnolvwe@163.com
注：这个是配合s3_read_score.py程序的写入程序
'''
import os
import tools
import random
# here put the import lib
with open("student_score.txt","w") as f:
    for i in range(10):
        f.write(str(random.randint(180000,190000)))
        f.write(",")
        f.write(tools.random_name())
        f.write(",")
        f.write(str(random.randint(60,100)))
        f.write("\n")
print("随机生成完成")