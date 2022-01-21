# coding: utf-8
# @Author : lryself
# @Date : 2021/2/2 23:29
# @Software: PyCharm

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        temp = {}
        result = 0
        while right < len(s):
            if not temp.get(s[right]):
                temp[s[right]] = 0
            temp[s[right]] += 1
            while sum(temp.values()) - max(temp.values()) > k:
                result = max(result, sum(temp.values()) - 1)
                temp[s[left]] -= 1
                left += 1
            right += 1
        return max(result, sum(temp.values()))
