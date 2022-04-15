# coding: utf-8
# @Author : lryself
# @Date : 2020/11/18 19:33
# @Software: PyCharm

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == denominator:
            return str(1)
        if numerator == 0:
            return str(0)
        w = ""
        if numerator < 0 or denominator < 0:
            if not (numerator < 0 and denominator < 0):
                w = "-"
        numerator = abs(numerator)
        denominator = abs(denominator)
        p = int(numerator / denominator)
        if numerator % denominator == 0:
            return w + str(p)
        numerator = numerator % denominator
        r = ""
        while numerator % denominator != 0 and len(r) <= 10 ** 4 + 2:
            r += str(int(numerator * 10 / denominator))
            numerator = numerator * 10 % denominator

        if len(r) < 10 ** 4 + 2:
            return "{}{}.{}".format(w, p, r)
        ch_map = {}
        for index, i in enumerate(r):
            if not ch_map.get(i):
                ch_map[i] = []
            ch_map[i].append(index)
        n = 0
        for k, v in ch_map.items():
            if len(v) < 3:
                continue
            for i in range(1, len(v) - 2):
                if r[v[0]:v[i]] == r[v[i]:v[i + i]]:
                    n = max(v[i + i] - v[i], n)
                    break
        for i in range(len(r) - n):
            if r[i:i + n] == r[i + n:i + 2 * n]:
                return "{}{}.{}({})".format(w, p, r[:i], r[i:i + n])
        return "0"


if __name__ == '__main__':
    s = Solution()
    print(s.fractionToDecimal(1, 214748364) == "0.00(000000465661289042462740251655654056577585848337359161441621040707904997124914069194026549138227660723878669455195477065427143370461252966751355553982241280310754777158628319049732085502639731402098131932683780538602845887105337854867197032523144157689601770377165713821223802198558308923834223016478952081795603341592860749337303449725)")
    print(s.fractionToDecimal(-50, 8))
    print(s.fractionToDecimal(-2147483648, 1))
    print(s.fractionToDecimal(1, 6))
    print(s.fractionToDecimal(35, 3))
    print(s.fractionToDecimal(1, 2))
    print(s.fractionToDecimal(2, 1))
    print(s.fractionToDecimal(1, 26))
    print(s.fractionToDecimal(1, 333))
    print(s.fractionToDecimal(4, 333))
