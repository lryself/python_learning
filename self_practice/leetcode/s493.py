# coding: utf-8
# @Author : lryself
# @Date : 2020/11/28 16:05
# @Software: PyCharm
from typing import List


def mager(nums: List[int]):
    if len(nums) == 1:
        return 0, nums
    num1 = nums[0:len(nums) // 2]
    num2 = nums[len(nums) // 2:]
    n1, num1 = mager(num1)
    n2, num2 = mager(num2)
    result = 0

    for i in num1:
        for index, j in enumerate(num2):
            if i > 2 * j:
                result += len(num2) - index
                break
    index = 0
    for i in num1:
        while index < len(num2):
            if i > num2[index]:
                num2.insert(index, i)
                break
            index += 1
        else:
            num2.append(i)
    return n1 + n2 + result, num2


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 0
        r, p = mager(nums)
        return r


if __name__ == '__main__':
    QAMap = [{"param": [], "answer": 0}]
