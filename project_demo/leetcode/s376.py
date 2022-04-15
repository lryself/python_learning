# coding: utf-8
# @Author : lryself
# @Date : 2020/12/12 20:07
# @Software: PyCharm
from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        i = 0
        result = []
        flag = 0
        while i + 1 < len(nums):
            if nums[i] != nums[i + 1]:
                result.append(nums[i])
                flag = 1 if nums[i] < nums[i+1] else -1
                if flag == 1:
                    while i + 1 < len(nums) and nums[i] < nums[i + 1]:
                        i += 1
                    result.append(nums[i])
                    i += 1
                    while i + 1 < len(nums) and nums[i] > nums[i + 1]:
                        i += 1
                else:
                    while i + 1 < len(nums) and nums[i] > nums[i + 1]:
                        i += 1
                    result.append(nums[i])
                    i += 1
                    while i + 1 < len(nums) and nums[i] < nums[i + 1]:
                        i += 1

            else:
                i += 1
        if len(result) == 0:
            return 1
        return len(result) if result[-1] == nums[-1] else len(result)+1
