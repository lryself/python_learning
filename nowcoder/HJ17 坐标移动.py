# coding: utf-8
# @Author : lryself
# @Date : 2022/6/26 16:48
# @Software: PyCharm
import re

sl = input().split(";")
x = 0
y = 0
for i in sl:
    if re.match(r"^[ADWS]\d{1,2}$", i):
        toward = i[0]
        location = eval(i[1:])
        if toward == "A":
            x -= location
        elif toward == "W":
            y += location
        elif toward == "D":
            x += location
        elif toward == "S":
            y -= location

print(f"{x},{y}")

