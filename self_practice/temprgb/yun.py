# coding: utf-8
# @Author : lryself
# @Date : 2021/3/9 21:44
# @Software: PyCharm
from pylab import *

with open("down.yuv", "rb") as f:
    data = f.read()
    data = [int(x) for x in data]

# 图像尺寸256*256*3
r = data[0:65535].copy()
g = data[65535:int(65535*1.25)]
b = data[int(65535*1.25):int(65535*1.5)]

r_color = {}
g_color = {}
b_color = {}

for i in range(256):
    r_color[i] = 0
    g_color[i] = 0
    b_color[i] = 0

for p in r:
    r_color[p] += 1

for p in g:
    g_color[p] += 1

for p in b:
    b_color[p] += 1

for color in r_color.keys():
    r_color[color] = r_color[color] / 65535

for color in g_color.keys():
    g_color[color] = g_color[color] / (65535 / 4)

for color in b_color.keys():
    b_color[color] = b_color[color] / (65535 / 4)

r_result = 0
g_result = 0
b_result = 0

for p in r_color.values():
    if p != 0:
        r_result += -p * log(p) / log(double(2))
for p in g_color.values():
    if p != 0:
        g_result += -p * log(p) / log(double(2))
for p in b_color.values():
    if p != 0:
        b_result += -p * log(p) / log(double(2))

print(r_result)
print(g_result)
print(b_result)

x_axis_data = [i for i in range(256)]

plt.plot(x_axis_data, r_color.values())
plt.plot(x_axis_data, g_color.values())
plt.plot(x_axis_data, b_color.values())

plt.show()
