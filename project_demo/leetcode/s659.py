# coding: utf-8
# @Author : lryself
# @Date : 2020/12/4 1:41
# @Software: PyCharm
from typing import List


class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        intmap = {}
        for i in nums:
            if intmap.get(i) is None:
                intmap[i] = 0
            intmap[i] += 1

        numslist = []
        for key, value in intmap.items():
            numslist.append([key, value])
        numslist.sort(key=lambda a: a[0])
        while len(numslist) > 0:
            count = 0
            before = 0
            before_num = 0
            for i in numslist:
                if before == 0:
                    before = i[0]
                    before_num = i[1]
                    i[1] -= 1
                    count += 1
                    continue
                if before != i[0] - 1:
                    if count < 3:
                        return False
                    break
                if before_num > i[1]:
                    if count < 3:
                        return False
                    break
                before = i[0]
                before_num = i[1]
                i[1] -= 1
                count += 1
            else:
                if count < 3:
                    return False
            i = 0
            while i < len(numslist):
                if numslist[i][1] <= 0:
                    numslist.__delitem__(i)
                    i -= 1
                i += 1
        return True
