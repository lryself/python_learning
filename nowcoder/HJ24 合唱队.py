# coding: utf-8
# @Author : lryself
# @Date : 2022/6/27 12:33
# @Software: PyCharm

def max_up_list(s):
    y = len(s)
    dp = [0 for _ in range(y)]
    for i in range(y):
        m = 0
        for j in range(i):
            if s[j] < s[i] and m < dp[j]:
                m = dp[j]
        dp[i] += m + 1
    return dp


def max_down_list(s):
    y = len(s)
    dp = [0 for _ in range(y)]
    for i in range(y-1, -1, -1):
        m = 0
        for j in range(i-1, y):
            if s[j] < s[i] and m < dp[j]:
                m = dp[j]
        dp[i] += m + 1
    return dp


n = eval(input())
l = list(map(int, input().split()))
dp1 = max_up_list(l)
dp2 = max_down_list(l)
max_x = 0
for i in range(n):
    if max_x < dp1[i]+dp2[i]-1:
        max_x = dp1[i]+dp2[i]-1

print(n - max_x)
