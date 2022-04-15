# coding: utf-8
# @Author : lryself
# @Date : 2020/11/22 10:44
# @Software: PyCharm
from queue import Queue


class Solution:
    def reverse(self, x: int) -> int:
        if not ((-2) ** 31) <= x <= ((2 ** 31) - 1):
            return 0
        c = 1
        if x < 0:
            c = -1
        s = str(abs(x))
        result = ""
        for ch in s:
            result = ch + result

        return c * int(result) if ((-2) ** 31) <= int(result) <= ((2 ** 31) - 1) else 0


if __name__ == '__main__':
    s = Solution()
    print(s.reverse(-123))
    print(s.reverse(1534236469))
