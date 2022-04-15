# coding: utf-8
# @Author : lryself
# @Date : 2020/12/14 0:40
# @Software: PyCharm
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]):
        import collections
        chlist = collections.defaultdict(list)
        for st in strs:
            chlist["".join(sorted(st))].append(st)

        return list(chlist.values())
