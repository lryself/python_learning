# coding: utf-8
# @Author : lryself
# @Date : 2021/3/9 17:24
# @Software: PyCharm
from pylab import *

with open("down.rgb", "rb") as f:
    data = f.read()
    data = [int(x) for x in data]

# 图像尺寸256*256*3
r = []
g = []
b = []
for index, rgb in enumerate(data):
    if index % 3 == 0:
        b.append(rgb)
    if index % 3 == 1:
        g.append(rgb)
    if index % 3 == 2:
        r.append(rgb)

r_color = {}
g_color = {}
b_color = {}

for i in range(257):
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
    r_color[color] = r_color[color] / (256 * 256)

for color in g_color.keys():
    g_color[color] = g_color[color] / (256 * 256)

for color in b_color.keys():
    b_color[color] = b_color[color] / (256 * 256)

r_result = 0
g_result = 0
b_result = 0

for p in r_color.values():
    if p != 0:
        r_result += -p * log(p)
for p in g_color.values():
    if p != 0:
        g_result += -p * log(p)
for p in b_color.values():
    if p != 0:
        b_result += -p * log(p)

print(r_result)
print(g_result)
print(b_result)

x_axis_data = [i for i in range(257)]

plt.plot(x_axis_data, r_color.values())
plt.plot(x_axis_data, g_color.values())
plt.plot(x_axis_data, b_color.values())

plt.show()
