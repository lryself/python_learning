# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import re
from numpy import mean


class MainSpiderPipeline:
    def __init__(self):
        self.f = open("result/positions.csv", "w", encoding="utf-8")
        self.f.write("职位,公司,工作地点,工资,发布时间\n")
        # 获取北京地区的平均薪酬
        self.count_salarys = []

    def process_item(self, item, spider):
        if item["salary"] == "":
            pass
        else:
            # 查找北京地区的职位
            if re.search("北京", item["site"]):
                salary_base = re.split("/", item["salary"])
                salary_cardinal = 1000.0
                if re.match(".*万$", salary_base[0]):
                    salary_cardinal = 10000
                if re.match("年", salary_base[1]):
                    salary_cardinal /= 12
                item_salarys = re.findall(r"\d+[.\d*]*", item["salary"])
                self.count_salarys.append((float(item_salarys[0]) + float(item_salarys[1]))/2*salary_cardinal)

            text = "{},{},{},{},{}".format(
                item["name"],
                item["company"],
                item["site"],
                item["salary"],
                item["date"])
            self.f.write(text)
            self.f.write("\n")
        return item

    def close_spider(self, spider):
        self.f.close()
        self.analyze_data()
        print("爬虫结束")

    def analyze_data(self):
        '''
        数据分析
        :return:
        '''
        with open("result/analyze.txt", "w", encoding="utf-8") as fi:
            fi.write("共统计找到{}个在北京的职位的数据\n".format(len(self.count_salarys)))
            fi.write(
                "北京地区python开发工程师的平均薪酬（月薪）为：{}\n".format(
                    mean(
                        self.count_salarys)))
            fi.write("北京地区python开发工程师的单个职位的最高平均薪酬（月薪）为：{}元/月\n".format(
                max(self.count_salarys)))
