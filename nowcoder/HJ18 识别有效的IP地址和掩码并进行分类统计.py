# coding: utf-8
# @Author : lryself
# @Date : 2022/6/26 17:05
# @Software: PyCharm
import re
import sys

x = 255
strl = []
i = 1
while x > 0:
    strl.append(x)
    x -= i
    i *= 2
print(strl)

A, B, C, D, E, Other, Private = 0, 0, 0, 0, 0, 0, 0
for line in sys.stdin:
    a = line.strip().split("~")
    ip = a[0]
    cover = a[1]

    flag_right = True

    # 判断掩码
    if re.match(r"^((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})(\.((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})){3}$", cover):
        if cover == "255.255.255.255" or cover == "0.0.0.0":
            flag_right = False
        covers = cover.split(".")
        flag_zero = False
        for i in covers:
            if flag_zero:
                if i != "0":
                    flag_right = False
                    break
                else:
                    continue
            if i != "255":
                flag_zero = True
            else:
                continue
            if not re.match(r"^1{0,8}0{0,7}$", str(bin(eval(i))).lstrip("0b")):
                flag_right = False
                break
            if eval(i) not in [255, 254, 252, 248, 240, 224, 192, 128, 0]:
                flag_right = False
                break

    else:
        flag_right = False

    # 判断IP
    if re.match(r"^((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})(\.((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})){3}$", ip):
        ips = ip.split(".")
        i = eval(ips[0])
        if i == 0 or i == 127:
            continue
        elif not flag_right:
            Other += 1
            continue
        if 1 <= i <= 126:
            A += 1
            if i == 10:
                Private += 1
        elif 128 <= i <= 191:
            B += 1
            if i == 172:
                j = eval(ips[1])
                if 16 <= j <= 32:
                    Private += 1
        elif 192 <= i <= 223:
            C += 1
            if ips[0] == "192" and ips[1] == "168":
                Private += 1
        elif 224 <= i <= 239:
            D += 1
        elif 240 <= i <= 255:
            E += 1
    else:
        flag_right = False
    if not flag_right:
        Other += 1
        continue

print(f"{A} {B} {C} {D} {E} {Other} {Private}")
