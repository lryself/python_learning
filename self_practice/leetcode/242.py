# coding: utf-8
# @Author : lryself
# @Date : 2020/11/22 1:36
# @Software: PyCharm
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chmap = {}
        for ch in s:
            if not chmap.get(ch):
                chmap[ch] = 0
            chmap[ch] += 1

        for ch in t:
            if not chmap.get(ch):
                return False
            chmap[ch] -= 1
        for i in chmap.values():
            if i != 0:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    if not s.isAnagram("anagram", "nagaram"):
        print("error:", "anagram", "nagaram")
    if s.isAnagram(s="rat", t="car"):
        print("error:", "rat", "car")
