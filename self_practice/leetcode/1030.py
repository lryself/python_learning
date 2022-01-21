# coding: utf-8
# @Author : lryself
# @Date : 2020/11/17 20:28
# @Software: PyCharm
from typing import List


class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        rmap = {}
        rmax = 0
        for r in range(R):
            for c in range(C):
                rtemp = abs(r - r0) + abs(c - c0)
                rmax = max(rtemp, rmax)
                if not rmap.get(rtemp):
                    rmap[rtemp] = []
                rmap[rtemp].append([r, c])
        result = []
        for i in range(rmax+1):
            for j in rmap[i]:
                result.append(j)
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.allCellsDistOrder(R=1, C=2, r0=0, c0=0))
    print(s.allCellsDistOrder(R=2, C=2, r0=0, c0=1))
    print(s.allCellsDistOrder(R=2, C=3, r0=1, c0=2))
