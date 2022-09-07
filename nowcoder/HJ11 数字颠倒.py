# coding: utf-8
# @Author : lryself
# @Date : 2022/6/25 20:32
# @Software: PyCharm

s = input()
for i in range(len(s)):
    print(s[-i-1], end="")