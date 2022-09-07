# coding: utf-8
# @Author : lryself
# @Date : 2022/6/25 20:42
# @Software: PyCharm

sl = input().split()
print(sl[-1], end="")
for i in range(len(sl)-1):
    print(f" {sl[-i-2]}", end="")
