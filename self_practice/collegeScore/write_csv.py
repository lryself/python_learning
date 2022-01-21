# coding: utf-8
# @Author : lryself
# @Date : 2021/6/23 18:35
# @Software: PyCharm
import csv
import json


def make_data(year: int) -> list:
    school_info = {}
    with open("statics/urls.txt", "r", encoding="utf-8") as f:
        for line in f:
            school_id = line.strip().split("/")[-1]
            with open(f"school_info/{school_id}.json", "r", encoding="utf-8") as f1:
                school_info[school_id] = json.loads(f1.read())
    with open(f"school_score/{year}/special_score.json", "r", encoding="utf-8") as f:
        datas = json.loads(f.read())
    results = []
    for data in datas:
        result = {}
        result["学校名称"] = school_info.get(data.get("school_id")).get('name')
        if data.get("type") == "1":
            result["科类"] = "理科"
        elif data.get("type") == "2":
            result["科类"] = "文科"
        else:
            result["科类"] = "-"
        result["批次"] = data.get("local_batch_name")
        result["平均分"] = data.get("average")
        result["最高分"] = data.get("max")
        result["最低分"] = data.get("min")
        result["最低位次"] = data.get("min_section")
        result["学位"] = data.get("level1_name")
        result["学科门类"] = data.get("level2_name")
        result["专业"] = data.get("level3_name")
        result["专业名称"] = data.get("spname")
        results.append(result)
    return results


if __name__ == '__main__':
    year = 2015
    with open(f"statics/{year}大学专业分数线表.csv", "w", encoding="utf-8", newline='') as f:
        headers = ['学校名称', '科类', '批次', '平均分', '最高分', "最低分", "最低位次", "学位", "学科门类", "专业", "专业名称"]
        f_csv = csv.DictWriter(f, headers)
        f_csv.writeheader()
        f_csv.writerows(make_data(year))
