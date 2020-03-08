# -*- encoding: utf-8 -*-
"""
@File : s1_search_print
@Time : 2020/3/4 19:54
@Author : lryself
@Version : 1.0
@Contact : lnolvwe@163.com
"""
"""
题目：元素输出和查找： 请输出0-50之间的奇数，偶数，质数；能同时被2和3整除的数；
"""
# here put the import lib
nums = list(range(51))
odds = []
evens = []
primes = []
nums1 = []
for a in nums:
    if a % 2 != 0:
        odds.append(a)
    else:
        evens.append(a)
        if a % 3 == 0:
            nums1.append(a)
    if a > 1:
        for b in range(2, a):
            if a % b == 0:
                break
        else:
            primes.append(a)
print("0~50之间的奇数有：")
print(odds)
print("0~50之间的偶数有：")
print(evens)
print("0~50之间的质数有：")
print(primes)
print("0~50之间能同时被2和3整除的数有：")
print(nums1)