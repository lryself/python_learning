# coding: utf-8
# @Author : lryself
# @Date : 2020/12/4 1:02
# @Software: PyCharm
from math import sqrt


class Solution:
    def countPrimes(self, n: int) -> int:
        count = 0
        for number in range(n):
            if number < 2:
                continue
            if number == 2 or number == 3:
                count += 1
                continue
            if number % 6 != 1 and number % 6 != 5:
                continue
            temp = int(sqrt(number))
            for i in range(5, temp + 1, 6):
                if number % i == 0 or number % (i + 2) == 0:
                    break
            else:
                count += 1
        return count
