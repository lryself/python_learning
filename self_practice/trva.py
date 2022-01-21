# coding: utf-8
# @Author : lryself
# @Date : 2021/1/5 22:35
# @Software: PyCharm
import requests
from bs4 import BeautifulSoup
import pymysql
import time


class Administrative(object):
    def __init__(self):
        self.db = pymysql.connect("rm-2ze3fpg05twt5cxh3125010dm.mysql.rds.aliyuncs.com", "power_china_2021", "powerChina2021", "powerchinadb", charset="utf8mb4")
        self.main()
        self.db.close()

    def main(self):
        base_url = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2018/'
        trs = self.get_response(base_url, 'provincetr')
        datas = []
        for tr in trs:  # 循环每一行
            for td in tr:  # 循环每个省
                province_name = td.a.get_text()
                province_url = base_url + td.a.get('href')
                print(province_name)
                trs = self.get_response(province_url, None)
                for tr in trs[1:]:  # 循环每个市
                    city_code = tr.find_all('td')[0].string
                    city_name = tr.find_all('td')[1].string
                    city_url = base_url + tr.find_all('td')[1].a.get('href')
                    trs = self.get_response(city_url, None)
                    for tr in trs[1:]:  # 循环每个区
                        county_code = tr.find_all('td')[0].string
                        county_name = tr.find_all('td')[1].string
                        data = [province_name, city_code, city_name, county_code, county_name]
                        print(data)
                        datas.append(data)
        print("爬取完成！")
        sql = "insert into china (province_name,city_code,city_name,county_code,county_name) values (%s,%s,%s,%s,%s)"
        self.connect_mysql(sql, datas)

    def get_response(self, url, attr):
        response = requests.get(url)
        response.encoding = 'gb2312'  # 编码转换
        soup = BeautifulSoup(response.text, 'lxml')
        table = soup.find_all('tbody')[1].tbody.tbody.table
        if attr:
            trs = table.find_all('tr', attrs={'class': attr})
        else:
            trs = table.find_all('tr')
        return trs

    def connect_mysql(self, sql, data):
        cursor = self.db.cursor()
        try:
            result = None
            if data:
                if isinstance(data[0], list):
                    cursor.executemany(sql, data)
                else:
                    cursor.execute(sql, data)
            else:
                cursor.execute(sql)
                result = cursor.fetchall()
        except Exception as e:
            print(e)
            self.db.rollback()
        finally:
            cursor.close()
            self.db.commit()  # 提交操作
            return result


if __name__ == '__main__':
    Administrative()