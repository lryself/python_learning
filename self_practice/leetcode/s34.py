# coding: utf-8
# @Author : lryself
# @Date : 2020/12/1 18:43
# @Software: PyCharm
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        if len(nums) == 1:
            return [-1, -1] if nums[0] != target else [0, 0]
        index = len(nums) // 2
        if nums[index] < target:
            result = self.searchRange(nums[index:], target)
            if result[0] != -1 and result[1] != -1:
                result[0] += index
                result[1] += index
        elif nums[index] > target:
            result = self.searchRange(nums[:index], target)
        else:
            s1 = self.searchRange(nums[:index], target)
            s2 = self.searchRange(nums[index:], target)
            result = [-1, -1]
            result[0] = s1[0] if s1[0] != -1 else s2[0] + index if s2[0] != -1 else -1
            result[1] = s2[1] + index if s2[1] != -1 else s1[1]
        return result
