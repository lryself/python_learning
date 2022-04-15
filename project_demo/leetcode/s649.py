# coding: utf-8
# @Author : lryself
# @Date : 2020/12/11 21:53
# @Software: PyCharm

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        passlist = {"R": 0, "D": 0}
        i = 0
        while senate.count("D") != 0 and senate.count("R") != 0:
            if i >= len(senate):
                i = 0
            if senate[i] == 'R':
                if passlist["R"] > 0:
                    passlist["R"] -= 1
                    senate = senate[:i] + senate[i + 1:]
                else:
                    passlist["D"] += 1
                    i += 1
            else:
                if passlist["D"] > 0:
                    passlist["D"] -= 1
                    senate = senate[:i] + senate[i + 1:]
                else:
                    passlist["R"] += 1
                    i += 1
        if senate.count("D") == 0:
            return "Radiant"
        else:
            return "Dire"
