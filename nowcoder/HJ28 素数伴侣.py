# coding: utf-8
# @Author : lryself
# @Date : 2022/7/2 20:15
# @Software: PyCharm

def is_prime(a: int) -> bool:
    if a % 2 == 0:
        return False
    x = a ** 0.5
    for i in range(3, int(x) + 2, 2):
        if a % i == 0:
            return False
    return True


# 取数
n = eval(input())
s = list(map(int, input().split()))
s.sort()

num_count = {}

simple = []
double = []
cp = {}

for i in s:
    cp[i] = []

for i in range(len(s)):
    if s[i] % 2 == 0:
        double.append(s[i])
    else:
        simple.append(s[i])
    for j in range(i + 1, len(s)):
        if is_prime(s[i] + s[j]):
            cp[s[i]].append(s[j])
            cp[s[j]].append(s[i])


def count_list(a, b):
    result = 0
    for i in a:
        for j in cp[i]:
            if j in b:
                result += 1
                b.remove(j)
                break
    return result


simple.sort(key=lambda a: len(cp[a]))
double.sort(key=lambda a: len(cp[a]))
for k in cp.keys():
    if k % 2 == 0:
        cp[k].sort(key=lambda x: simple.index(x))
    else:
        cp[k].sort(key=lambda x: double.index(x))
if len(simple) < len(double):
    print(count_list(simple, double))
else:
    print(count_list(double, simple))
