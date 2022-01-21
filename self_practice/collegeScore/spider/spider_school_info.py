# coding: utf-8
# @Author : lryself
# @Date : 2021/6/23 18:56
# @Software: PyCharm
import json
from multiprocessing import cpu_count, Pool

import requests


def main():
    pool = Pool(cpu_count() * 2 + 1)
    with open("../statics/urls.txt", "r", encoding="utf-8") as f:
        for line in f:
            school_id = line.strip().split("/")[-1]

            pool.apply_async(download_json, (school_id,))

        pool.close()
        pool.join()


def download_json(school_id):
    response = requests.get(
        url=f"https://static-data.eol.cn/www/2.0/school/{school_id}/info.json",
    )
    with open(f"school_info/{school_id}.json", "w", encoding="utf-8") as f:
        f.write(json.dumps(read_json(response.text)))
    print(f"完成{school_id}")


def read_json(j: str) -> dict:
    t = json.loads(j)
    return t['data']


if __name__ == '__main__':
    main()
