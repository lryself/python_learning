# coding: utf-8
# @Author : lryself
# @Date : 2021/2/4 15:24
# @Software: PyCharm

from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        result = []
        n = len(nums)
        result.append(0)
        for i in range(0, k):
            result[0] += nums[i]
        for i in range(1, n-k+1):
            result.append(result[-1]-nums[i-1]+nums[i+k-1])
        return max(result)/k


if __name__ == '__main__':
    s = Solution()
    print(s.findMaxAverage([7, 4, 5, 8, 8, 3, 9, 8, 7, 6], 7))
