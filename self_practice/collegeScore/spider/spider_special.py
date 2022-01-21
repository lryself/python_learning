# coding: utf-8
# @Author : lryself
# @Date : 2021/6/23 16:34
# @Software: PyCharm
import json
from multiprocessing import cpu_count, Pool
import requests


def read_json(j: str) -> list:
    t = json.loads(j)
    return t['data']['item']


def download_schoolSpecialIndex_json(year, schoolID, province, subject, dic):
    result = []
    response = requests.get(
        url=f"https://static-data.eol.cn/www/2.0/schoolspecialindex/{year}/{schoolID}/{province}/{subject}/{dic}/1.json",
    )
    t = response.text
    if t == "\"\"":
        return []
    data = json.loads(t)
    n = int(data['data']['numFound'])
    result.extend(data['data']['item'])
    for page in range(2, (n - 1) // 10 + 1 + 1):
        response = requests.get(
            url=f"https://static-data.eol.cn/www/2.0/schoolspecialindex/{year}/{schoolID}/{province}/{subject}/{dic}/{page}.json",
        )
        if t == "\"\"":
            continue
        r = response.text
        data = json.loads(r)
        result.extend(data['data']['item'])
    return result


def spider_all_json(year, schoolID):
    result = []
    result.extend(download_schoolSpecialIndex_json(year, schoolID, 64, 1, 7))
    result.extend(download_schoolSpecialIndex_json(year, schoolID, 64, 2, 7))
    result.extend(download_schoolSpecialIndex_json(year, schoolID, 64, 1, 8))
    result.extend(download_schoolSpecialIndex_json(year, schoolID, 64, 2, 8))

    with open(f"school_score/{year}/{schoolID}.json", "w", encoding="utf-8") as f:
        f.write(json.dumps(result))
    print(f"已完成{schoolID}")


# if __name__ == '__main__':
#     year = 2020
#     schoolID = 140
#     province = 64
#     # 理科 - 1 文科 - 2
#     subject = 1
#     # 本科一批 - 1 本科二批 - 2
#     dic = 7
#     print(download_schoolSpecialIndex_json(year, schoolID, province, subject, dic))
#     "https://static-data.eol.cn/www/2.0/school/140/info.json"

def main():
    pool = Pool(cpu_count() * 2 + 1)
    print("开始运行")
    with open("../urls.txt", "r", encoding="utf-8") as f:
        for line in f:
            school_id = line.strip().split("/")[-1]
            for year in range(2015, 2021):
                pool.apply_async(spider_all_json, (year, school_id,))
    pool.close()
    pool.join()


if __name__ == '__main__':
    main()
