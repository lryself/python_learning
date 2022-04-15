# coding: utf-8
# @Author : lryself
# @Date : 2021/6/20 22:08
# @Software: PyCharm
import json

import requests


def get_pro() -> str:
    with open("statics/dic.json", "r", encoding="utf-8") as f:
        pro = json.loads(f.read())
    return pro['data']


def get_pro_min_by_id(ID: str):
    pros = get_pro()
    with open(f"school_info/{ID}.json", "r", encoding="utf-8") as f:
        pro = json.loads(f.read())
    return_list = []
    for d in pro['data']['pro_type_min']['64']:
        return_dict = {'year': d['year'], 'type': {}}
        for k, v in d['type'].items():
            return_dict['type'][pros[k]] = v
        return_list.append(return_dict)
    return return_list


def get_school_info_json(schoolID: str):
    response = requests.get(f"https://static-data.eol.cn/www/2.0/school/{schoolID}/info.json")
    with open(f"school_info/{schoolID}.json", "w", encoding="utf-8") as f:
        f.write(response.text)


def get_json() -> str:
    with open("school_info/140.json", "r", encoding="utf-8") as f:
        data = json.loads(f.read())
    return data


if __name__ == '__main__':
    get_json()
    # print(get_score())
