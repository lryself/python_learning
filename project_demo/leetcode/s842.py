# coding: utf-8
# @Author : lryself
# @Date : 2020/12/8 3:24
# @Software: PyCharm
from typing import List


class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        n = len(S)
        maxint = 2 ** 31 - 1

        def makefib(a: int, b: int):
            result1 = "{}{}".format(a, b)
            result2 = [a, b]
            while len(result1) < n:
                temp = result2[-2] + result2[-1]
                if temp > maxint:
                    return "", []
                result1 += str(temp)
                result2.append(temp)
            return result1, result2

        if n < 3 or S[0] == 0:
            return []
        i = 1
        while i < n - 1:
            if S[i] == 0:
                continue
            first = int(S[:i])
            if first > maxint:
                return []
            j = i + 1
            second = 0
            while j < n:
                if S[j] == 0:
                    continue
                second = int(S[i:j])
                if second > maxint:
                    break
                w = j + (j - i)
                third = 0
                while w < n + 1:
                    third = int(S[j:w])
                    if third > maxint:
                        break
                    if first + second <= third:
                        if first + second < third:
                            break
                        elif first + second == third:
                            temp1, temp2 = makefib(first, second)
                            if temp1 == S:
                                return temp2
                            elif temp1 == "":
                                return []
                    w += 1
                j += 1
            i += 1
        return []
