# coding: utf-8
# @Author : lryself
# @Date : 2021/2/3 12:15
# @Software: PyCharm
from typing import List
from numpy import median


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        result = []
        for i in range(0, len(nums)-k+1):
            result.append(float(median(nums[i:i+k])))
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.medianSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
