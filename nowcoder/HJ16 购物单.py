# coding: utf-8
# @Author : lryself
# @Date : 2022/6/25 22:27
# @Software: PyCharm
m, n = map(int, input().split())
w, v = [], []
p, q = {}, {}
for i in range(1, n+1):
    x, y, z = map(int, input().split())
    if z == 0:
        p[i] = [x, y]
    else:
        if z in q:
            q[z].append([x, y])
        else:
            q[z] = [[x, y]]
n = len(p)
for i in p.keys():
    w.append(p[i][0])
    v.append(p[i][1]*p[i][0])
    if i in q:
        t = q[i]
        w.append(p[i][0] + t[0][0])
        v.append(p[i][1]*p[i][0] + t[0][0]*t[0][1])
        if len(q[i]) == 2:
            w.append(p[i][0] + t[1][0])
            v.append(p[i][1]*p[i][0] + t[1][0]*t[1][1])
            w.append(p[i][0] + t[0][0] + t[1][0])
            v.append(p[i][1]*p[i][0] + t[0][0]*t[0][1] + t[1][0]*t[1][1])
n = len(w)
dp = [[0]*(m+1) for _ in range(n+1)]
for i in range(1, n + 1):
    for j in range(10, m + 1, 10):
        if j - w[i-1] >= 0:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i-1]] + v[i-1])
        else:
            dp[i][j] = dp[i-1][j]
print(dp[n][m])
