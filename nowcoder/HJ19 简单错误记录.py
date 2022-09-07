# coding: utf-8
# @Author : lryself
# @Date : 2022/6/26 18:19
# @Software: PyCharm
import sys

d = {}
li = {}
index = 0
for line in sys.stdin:
    index += 1
    a = line.split()
    name = a[0].split("\\")[-1]
    if len(name) > 16:
        name = name[-16:]
    key = f"{name} {a[1]}"
    if not li.get(key):
        li[key] = index
    if d.get(key):
        d[key] += 1
    else:
        d[key] = 1

output = list(li.keys())
output.sort(key=lambda x: li[x])
for i in output[-8:]:
    print(f"{i} {d[i]}")
