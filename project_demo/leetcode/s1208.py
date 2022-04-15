# coding: utf-8
# @Author : lryself
# @Date : 2021/2/5 9:28
# @Software: PyCharm


class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        change_list = []
        for i in range(n):
            change_list.append(abs(ord(s[i]) - ord(t[i])))
        left = right = 0
        result = 0
        sums = 0
        while right < n:
            sums += change_list[right]
            while sums > maxCost:
                sums -= change_list[left]
                left += 1
            result = max(result, right - left + 1)
            right += 1
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.equalSubstring("krrgw", "zjxss", 19) == 2)
    print(s.equalSubstring("abcd", "bcdf", 3) == 3)
    print(s.equalSubstring("abcd", "cdef", 3) == 1)
    print(s.equalSubstring("abcd", "acde", 0) == 1)
