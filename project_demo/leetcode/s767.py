# coding: utf-8
# @Author : lryself
# @Date : 2020/11/30 16:48
# @Software: PyCharm

class Solution:
    def reorganizeString(self, S: str) -> str:
        chmap = {}
        for s in S:
            if chmap.get(s) is None:
                chmap[s] = 0
            chmap[s] += 1
        for c in chmap.values():
            if c > (len(S) + 1) // 2:
                return ''
        result = ''
        chlist = []
        for i in chmap.items():
            chlist.append([i[0], i[1]])
        chlist.sort(key=lambda a: a[1], reverse=True)
        while len(result) < len(S):
            for c in chlist:
                if c[1] > 0 and (c[0] != result[-1]) if len(result) > 0 else True:
                    result += c[0]
                    c[1] -= 1
                    if c[1] <= 0:
                        chlist.remove(c)
                    break
            else:
                for c in chlist:
                    for index, i in enumerate(result):
                        if result[index + 1] != c[0] and i != c[0]:
                            result = result[:index + 1] + c[0] + result[index + 1:]
                            c[1] -= 1
                            if c[1] <= 0:
                                chlist.remove(c)
                            break
        return result
