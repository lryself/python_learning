# here put the import lib
# @Time : 2020/9/3 20:17
# @Author : liruiyang
# @File : test
# @Software: PyCharm
import datetime
from time import sleep

import xlwt
from bs4 import BeautifulSoup
from selenium import webdriver


def gethtml1(path, url):
    option = webdriver.ChromeOptions()
    option.add_argument('headless')

    # browser = webdriver.Chrome(executable_path=path, options=option)
    browser = webdriver.Chrome(executable_path=path)
    # 进入无头模式更换上列代码
    htmls = []
    try:
        browser.get(url)
        sleep(1)
        pages = browser.find_element_by_xpath('//div[@id="pagebar"]//label[last()-1]').text
        htmls.append(browser.page_source)
        for i in range(int(pages)-1):
        # for i in range(1):
            try:
                browser.find_element_by_xpath('//div[@id="pagebar"]//label[last()]').click()
                sleep(6)
                htmls.append(browser.page_source)
                print("已爬取{}页".format(i+1))
            except Exception as e:
                print("第{}页出现问题".format(i+1))
    except Exception as e:
        print(e)
        return False
    else:
        return htmls
    finally:
        browser.close()


def gethtml2(path, url):
    option = webdriver.ChromeOptions()
    option.add_argument('headless')

    browser = webdriver.Chrome(executable_path=path, options=option)
    # browser = webdriver.Chrome(executable_path=path)
    # 进入无头模式更换上列代码
    htmls = []
    try:
        browser.get(url)
        sleep(6)
        pages = browser.find_element_by_xpath('//div[@id="pager"]//li[last()-1]').text
        htmls.append(browser.page_source)
        for i in range(int(pages)-1):
        # for i in range(5):
            browser.find_element_by_xpath('//div[@id="pager"]//li[last()]').click()
            sleep(6)
            htmls.append(browser.page_source)
            print("已爬取{}页".format(i+1))
    except Exception as e:
        print(e)
        return False
    else:
        return htmls
    finally:
        browser.close()


def spider_data(response, row, worksheet):
    soup = BeautifulSoup(response, 'html.parser')
    for i, children in enumerate(soup.find("table", id="dbtable").find_all("tr")):
        if i == 0:
            continue
        lum_list = []
        for lum, td in enumerate(children.find_all("td")):
            if 2 <= lum <= 19:
                lum_list.append(td.text)
        write_row(lum_list, row, worksheet)
        row += 1
    return row


def write_row(list1, row, worksheet):
    for lum in range(len(list1)):
        worksheet.write(row, lum, list1[lum])


def main1():
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('sheet1')
    style = xlwt.XFStyle()  # 初始化样式
    font = xlwt.Font()  # 为样式创建字体
    font.name = 'Times New Roman'
    font.bold = False  # 黑体
    font.underline = False  # 下划线
    font.italic = False  # 斜体字
    style.font = font  # 设定样式
    write_row(("基金代码","基金简称","日期","单位净值","累计净值","日增长率","近1周","近1月","近3月","近6月","近1年","近2年","近3年","今年来","成立来","自定义","手续费"),
              0, worksheet)
    row = 1

    search_url = "http://fund.eastmoney.com/data/fundranking.html#tall;c0;r;s1yzf;pn50;ddesc;qsd20200106;qed20210106;qdii;zq;gg;gzbd;gzfs;bbzt;sfbb"
    responses = gethtml1(path='D:\software\chromedriver.exe', url=search_url)

    for response in responses:
        row = spider_data(response=response, row=row, worksheet=worksheet)

    workbook.save("{}.xls".format(datetime.datetime.now().strftime('%Y%m%d%H%M%S')))
    print("输出完成")


if __name__ == '__main__':
    main1()
    # workbook = xlwt.Workbook(encoding='utf-8')
    # worksheet = workbook.add_sheet('sheet1')
    # style = xlwt.XFStyle()  # 初始化样式
    # font = xlwt.Font()  # 为样式创建字体
    # font.name = 'Times New Roman'
    # font.bold = False  # 黑体
    # font.underline = False  # 下划线
    # font.italic = False  # 斜体字
    # style.font = font  # 设定样式
    # write_row(("代码","简称","单位净值","日期","近1年定投收益","近2年定投收益","近3年定投收益","近5年定投收益","上海证券评级06-30","手续费"), 0)
    # row = 1
    #
    # search_url = "http://fund.eastmoney.com/dingtou/syph_yndt.html"
    # responses = gethtml2(path='D:\CodeApp\chromedriver.exe', url=search_url)
    #
    # for response in responses:
    #     spider_data(response)
    #
    # workbook.save("temp1.xls")
    # print("输出完成")