# coding: utf-8
# @Author : lryself
# @Date : 2020/11/22 12:18
# @Software: PyCharm

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x == 0:
            return True
        s = str(x)
        s1 = ""
        for ch in s:
            s1 = ch + s1
        if s == s1:
            return True
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome(-123))
