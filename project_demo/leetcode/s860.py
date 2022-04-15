# coding: utf-8
# @Author : lryself
# @Date : 2020/12/10 0:23
# @Software: PyCharm
from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        ch5 = 0
        ch10 = 0
        ch20 = 0
        for bill in bills:
            if bill == 20:
                ch20 += 1
                if ch10 > 0:
                    ch10 -= 1
                    ch5 -= 1
                else:
                    ch5 -= 3
            elif bill == 10:
                ch10 += 1
                ch5 -= 1
            else:
                ch5 += 1
            if ch5 < 0:
                return False
        else:
            return True
