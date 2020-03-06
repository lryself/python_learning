# -*- encoding: utf-8 -*-
'''
@File : 练习四.py
@Time : 2020/03/04 09:15:37
@Author : lryself 
@Version : 1.0
@Contact : lryself@163.com
'''

# here put the import lib
'''题目：创建一个有10个数字的列表,先输出此列表，并且输出其中的偶数元素;
'''
s=list(range(10,20))
for a in s:
    print(a)
print()
for a in s:
    if a%2==0:
        print(a)