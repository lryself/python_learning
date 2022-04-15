# -*- encoding: utf-8 -*-
'''
@File : s5_copytxt.py
@Time : 2020/03/27 18:19:55
@Author : lryself 
@Version : 1.0
@Contact : lnolvwe@163.com
题目：通过Python来模拟实现一个txt文件的拷贝过程
'''
import tools
# here put the import lib
try:
    f1=open(input("请输入您要拷贝的txt文件位置(绝对路径)"),"r",encoding="utf-8")
    f2=open(input("请输入您要拷贝txt文件到哪里？(绝对路径)"),"w",encoding="utf-8")
except OSError:
    print("文件路径错误")
else:
    for line in f1:
        f2.write(line)
finally:
    print("拷贝完成！")
    f1.close()
    f2.close()
