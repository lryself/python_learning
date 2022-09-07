# coding: utf-8
# @Author : lryself
# @Date : 2022/6/25 22:08
# @Software: PyCharm
x = eval(input())
r = 0
while x != 0:
    if x % 2 != 0:
        r += 1
    x = x // 2
print(r)