# coding: utf-8
# @Author : lryself
# @Date : 2022/7/1 21:37
# @Software: PyCharm

I = input().split()[1:]
R = list(set(map(int, input().split()[1:])))
R.sort()
R = list(map(str, R))
RMap = {}
for i in R:
    RMap[i] = []

for index, i in enumerate(I):
    v = [index, i]
    for j in R:
        if j in i:
            RMap[j].append(v)

result = []
for k in R:
    v = RMap[k]
    if len(RMap[k]) == 0:
        continue

    result.append(k)
    result.append(len(v))
    for i in v:
        result.append(i[0])
        result.append(i[1])
print(len(result), end="")
for i in result:
    print(f" {i}", end="")
