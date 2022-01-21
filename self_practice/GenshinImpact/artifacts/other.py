# coding: utf-8
# @Author : lryself
# @Date : 2021/6/19 8:57
# @Software: PyCharm

def dpsCalculate(ATKPercentage, CRITDMG, CRITRate) -> float:
    return (1 + ATKPercentage * 0.01) * ((5 + CRITRate) * 0.01 * (150 + CRITDMG) * 0.01 + (1 - (5 + CRITRate) * 0.01))


if __name__ == '__main__':
    # resultDict = {}
    # allCombination = []
    # for ATKPercentage in range(0, 7 + 1):
    #     for CRITDMG in range(0, 7 - ATKPercentage + 1):
    #         for CRITRate in range(0, 7 - ATKPercentage - CRITDMG + 1):
    #             allCombination.append([ATKPercentage, CRITDMG, CRITRate])
    # maxResult1 = 0
    # maxResult2 = []
    # n = 0
    # for i in allCombination:
    #     for j in allCombination:
    #         for k in allCombination:
    #             for l in allCombination:
    #                 s = [i[0] + j[0] + k[0] + l[0], i[1] + j[1] + k[1] + l[1], i[2] + j[2] + k[2] + l[2]]
    #                 temp = dpsCalculate(s[0], s[1], s[2])
    #                 if maxResult1 < temp:
    #                     maxResult1 = temp
    #                     maxResult2 = [s]
    #                 elif maxResult1 == temp:
    #                     maxResult2.append(s)
    #                 if n % 20736 == 0:
    #                     print(f"进度：{n // 20736}/10000")
    #                     n += 1
    # print(maxResult1, maxResult2)
    print(dpsCalculate(4, 50.2, 111.7))
