# coding: utf-8
# @Author : lryself
# @Date : 2020/11/27 15:07
# @Software: PyCharm
from typing import List


class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        intmap = {}
        result = 0
        for a in A:
            for b in B:
                if not intmap.get(a + b):
                    intmap[a + b] = 0
                intmap[a + b] += 1
        for c in C:
            for d in D:
                if intmap.get(-c - d):
                    result += intmap[-c-d]
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.fourSumCount([1, 2], [-2, -1], [-1, 2], [0, 2]))
    print(s.fourSumCount([-1, -1], [-1, 1], [-1, 1], [1, -1]))
