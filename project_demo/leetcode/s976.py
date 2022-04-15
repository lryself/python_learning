# coding: utf-8
# @Author : lryself
# @Date : 2020/11/29 17:05
# @Software: PyCharm
from typing import List


class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort(reverse=True)
        for index in range(len(A) - 2):
            temp = A[index:index + 3]
            if A[index] + A[index + 1] <= A[index + 2]:
                continue
            elif A[index] - A[index + 1] >= A[index + 2]:
                continue
            return sum(temp)
        else:
            return 0
