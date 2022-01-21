# coding: utf-8
# @Author : lryself
# @Date : 2021/1/7 0:16
# @Software: PyCharm
import datetime
import json
import multiprocessing

import requests
import re
import csv

import xlwt
from selenium import webdriver


def get_respones(p):
    header = {
        "Host": "fund.eastmoney.com",
        "Referer": "http://fund.eastmoney.com/data/fundranking.html"
    }
    params = {
        "op": "ph",
        "dt": "kf",
        "ft": "all",
        "gs": "0",
        "sc": "1yzf",
        "st": "desc",
        "sd": (datetime.datetime.now()-datetime.timedelta(days=365)).strftime('%Y-%m-%d'),
        "ed": datetime.datetime.now().strftime('%Y-%m-%d'),
        "pi": f"{p}",
        "pn": "50",
        "dx": "1",
        "v": "0.1"
    }
    result = requests.get(url="http://fund.eastmoney.com/data/rankhandler.aspx", headers=header, params=params)
    # re_data(result.text, writer)
    print("完成{}页".format(p))
    return result.text


def re_data(html_str):
    json_data = re.search("datas:\[.+\]", html_str).group().strip("datas:")
    data_list = json.loads(json_data)
    result = []
    for row in data_list:
        result1 = []
        for i, lum in enumerate(row.split(",")):
            if i not in [2, 3, 16, 17, 19, 21, 22, 23, 24]:
                if lum == "":
                    result1.append("---")
                elif i not in [0, 1, 4, 5, 20]:
                    result1.append(lum + "%")
                else:
                    result1.append(lum)
        result.append(result1)
    return result


def write_row(list1, row, worksheet):
    for lum in range(len(list1)):
        worksheet.write(row, lum, list1[lum])


def get_pages() -> int:
    option = webdriver.ChromeOptions()
    option.add_argument('headless')

    # browser = webdriver.Chrome(executable_path=path, options=option)
    browser = webdriver.Chrome(executable_path='D:\software\chromedriver.exe', options=option)
    # 进入无头模式更换上列代码
    p = 0
    try:
        browser.get("http://fund.eastmoney.com/data/fundranking.html")
        p = browser.find_element_by_xpath('//*[@id="pagebar"]/label[7]').text
    except Exception as e:
        print(e)
    finally:
        browser.close()
        return int(p)


# 2,3,16,17,19,21,22,23,24
if __name__ == '__main__':
    pages = get_pages()
    print(f"共计{pages}页")
    print("开始爬取")
    pool = multiprocessing.Pool(multiprocessing.cpu_count()*2+1)
    datas = []
    for page in range(1, pages + 1):
        result = pool.apply_async(func=get_respones, args=(page,))
        datas.append((page, result))
    pool.close()
    pool.join()
    print("爬取完成")
    datas.sort(key=lambda a: a[0])

    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('sheet1')
    style = xlwt.XFStyle()  # 初始化样式
    font = xlwt.Font()  # 为样式创建字体
    font.name = 'Times New Roman'
    font.bold = False  # 黑体
    font.underline = False  # 下划线
    font.italic = False  # 斜体字
    style.font = font  # 设定样式
    write_row(("基金代码", "基金简称", "单位净值", "累计净值", "日增长率", "近1周", "近1月", "近3月", "近6月", "近1年", "近2年", "近3年", "今年来",
               "成立来", "自定义", "手续费"),
              0, worksheet)
    row = 1

    result_data = []
    for data in datas:
        result_data.extend(re_data(data[1].get()))
    for data in result_data:
        write_row(data, row, worksheet)
        row += 1

    workbook.save("{}.xls".format(datetime.datetime.now().strftime('%Y%m%d%H%M%S')))
    print("输出完成")
