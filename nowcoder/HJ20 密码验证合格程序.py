# coding: utf-8
# @Author : lryself
# @Date : 2022/6/27 11:36
# @Software: PyCharm
import re
import sys

for line in sys.stdin:
    # a,b,c,d分别为大写、小写、数字、其他符号
    line = line.strip()
    if len(line) < 8:
        print("NG")
        continue
    a, b, c, d = 0, 0, 0, 0
    temp_s = ""
    temp_d = {}
    for i in line:
        if re.match(r"\d", i):
            c = 1
        elif re.match(r"[a-z]", i):
            b = 1
        elif re.match(r"[A-Z]", i):
            a = 1
        elif i == " " or i == "\n":
            print("NG")
            break
        else:
            d = 1
        temp_s = temp_s + i
        if len(temp_s) >= 3:
            key = temp_s[-3:]
            if key in temp_d:
                print("NG")
                break
            temp_d[key] = 0
    else:
        if a + b + c + d >= 3:
            print("OK")
        else:
            print("NG")
