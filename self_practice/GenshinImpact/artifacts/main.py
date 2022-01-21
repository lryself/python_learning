# coding: utf-8
# @Author : lryself
# @Date : 2021/6/15 0:06
# @Software: PyCharm

from models import Flower, Plume, Sands, Goblet, Circlet
from BaseNumber import BaseNumericalDict, SpeciesCoefficientDict, CommonRoleWeaponsCoefficientDict, CommonRoleAttributeCoefficientDict


def get_one_artifact_score(artifact, role, attribute):
    artifact_name = artifact.__name__
    n = 0
    temp_dict = BaseNumericalDict
    temp_tuple = list(artifact.__dict__.items())
    flag = False
    for key, value in temp_tuple:
        if key == "Core":
            flag = True
        elif type(value) is tuple:
            n += value[0] / temp_dict[key] \
                 * SpeciesCoefficientDict[artifact_name][key] \
                 * CommonRoleWeaponsCoefficientDict[role][key] \
                 * CommonRoleAttributeCoefficientDict[attribute][key]
    if flag:
        return n*1.1
    return n


def calculate_score(role, attribute):
    n = 0
    flower_score = get_one_artifact_score(Flower, role, attribute)
    n += flower_score
    print("花的分数：", flower_score, "评级：", score_degree(flower_score))
    plume_score = get_one_artifact_score(Plume, role, attribute)
    n += plume_score
    print("羽的分数：", plume_score, "评级：", score_degree(plume_score))
    sands_score = get_one_artifact_score(Sands, role, attribute)
    n += sands_score
    print("沙的分数：", sands_score, "评级：", score_degree(sands_score))
    goblet_score = get_one_artifact_score(Goblet, role, attribute)
    n += goblet_score
    print("杯的分数：", goblet_score, "评级：", score_degree(goblet_score))
    circlet_score = get_one_artifact_score(Circlet, role, attribute)
    n += circlet_score
    print("头的分数：", circlet_score, "评级：", score_degree(circlet_score))

    print(f"总评得分：", n)
    if n > 65:
        print("评价结果： 大毕业")
    elif n > 57.3:
        print("评价结果： 小毕业")
    elif n > 49:
        print("评价结果： 合格")
    else:
        print("仍需努力")
    return n


def score_degree(score):
    if score > 16.67:
        return "Max"
    elif score > 16:
        return "SSR"
    elif score > 14:
        return "SR"
    elif score > 13.3:
        return "S+"
    elif score > 12.5:
        return "S"
    elif score > 11.8:
        return "S-"
    elif score > 11.1:
        return "A+"
    elif score > 10.6:
        return "A"
    elif score > 10.1:
        return "A-"
    elif score > 9.6:
        return "B+"
    elif score > 9.1:
        return "B"
    elif score > 8.6:
        return "B-"
    elif score > 8.1:
        return "C+"
    elif score > 7.6:
        return "C"
    elif score > 7.1:
        return "C-"
    elif score > 6.6:
        return "D+"
    elif score > 6.1:
        return "D"
    elif score > 5.6:
        return "D-"
    else:
        return "请升满20级"


if __name__ == '__main__':
    roleWeapons = "Sword"
    roleAttribute = "Electron"
    calculate_score(roleWeapons, roleAttribute)
