# coding: utf-8
# @Author : lryself
# @Date : 2021/5/19 23:11
# @Software: PyCharm
import csv
import json

if __name__ == '__main__':
    with open("Wuhan-2019-nCoV.json", "r", encoding="utf-8") as f:
        t = f.read()
    with open("nCov.csv", "w", encoding="utf-8") as f:
        tempList = json.loads(t)
        fieldnames = ["date", "country", "countryCode", "province", "provinceCode", "city", "cityCode", "confirmed",
                      "suspected", "cured", "dead"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for data in tempList:
            writer.writerow(data)
