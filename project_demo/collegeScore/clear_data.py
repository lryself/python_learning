# coding: utf-8
# @Author : lryself
# @Date : 2021/6/23 17:28
# @Software: PyCharm
import json

if __name__ == '__main__':
    year = 2015
    with open(f"school_score/{year}/special_score.json", "w", encoding="utf-8") as f:
        results = []
        with open("statics/urls.txt", "r", encoding="utf-8") as f1:
            for line in f1:
                school_id = line.strip().split("/")[-1]
                with open(f"school_score/{year}/{school_id}.json", "r", encoding="utf-8") as f2:
                    l = json.loads(f2.read())
                    results.extend(l)
        f.write(json.dumps(results))
