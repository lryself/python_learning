# coding: utf-8
# @Author : lryself
# @Date : 2020/11/19 12:45
# @Software: PyCharm
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = 0
        for index, num in enumerate(nums[:-n]):
            if num == 0:
                zreo.append(index)
        for index, n in enumerate(zreo):
            nums.__delitem__(n - index)
            nums.append(0)


if __name__ == '__main__':
    s = Solution()
    temps = [0, 1, 0, 3, 12]
    s.moveZeroes(temps)
    print(temps)
