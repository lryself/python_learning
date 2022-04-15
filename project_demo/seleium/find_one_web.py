# here put the import lib
# @Time : 2020/8/28 11:15
# @Author : liruiyang
# @File : test
# @Software: PyCharm
import datetime
from time import sleep
from selenium import webdriver


def gethtml(path, url):
    option = webdriver.ChromeOptions()
    option.add_argument('headless')

    browser = webdriver.Chrome(executable_path=path, options=option)
    # browser = webdriver.Chrome(executable_path=path)
    # 进入无头模式更换上列代码
    try:
        browser.get(url)
        sleep(1)
        html = browser.page_source
    except Exception as e:
        print(e)
        return False
    else:
        return html
    finally:
        browser.close()


if __name__ == '__main__':
    begin = datetime.datetime.now()
    search_url = 'http://www.deligent-tech.com'
    response = gethtml(path='D:\CodeApp\chromedriver.exe', url=search_url)
    end = datetime.datetime.now()
    print(end-begin)
    with open('test.html', 'w', encoding='utf-8') as f:
        f.write(response)