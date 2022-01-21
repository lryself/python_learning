# coding: utf-8
# @Author : lryself
# @Date : 2021/6/20 21:36
# @Software: PyCharm
import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


def get_html(chrome_path, url):
    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    # browser = webdriver.Chrome(executable_path=chrome_path, options=option)

    browser = webdriver.Chrome(executable_path=chrome_path)
    # 进入无头模式更换上列代码
    results = []
    try:
        with open("../statics/urls.txt", "w", encoding="utf-8") as f:
            browser.get(url)
            browser.maximize_window()
            time.sleep(1)
            browser.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div/div[1]/div[2]/div[3]/div/div[2]/p').click()
            time.sleep(1)
            browser.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div/div[1]/div[3]/div[2]/div[9]/div[2]/div[2]/a[1]').click()
            time.sleep(1)
            for page in range(61):
                try:
                    rows = len(browser.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div/div[1]/div[3]/div[1]/div/div[1]/table/tbody').find_elements_by_tag_name('tr'))
                except NoSuchElementException:
                    browser.refresh()
                    time.sleep(5)
                for row in range(rows):
                    browser.find_element_by_xpath(f'//*[@id="root"]/div/div/div/div/div/div[1]/div[3]/div[1]/div/div[1]/table/tbody/tr[{row+1}]/td[2]/div[1]/a').click()
                time.sleep(1)
                browser.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div/div[1]/div[3]/div[1]/div/div[2]/ul/li[10]').click()

                old_windows_handle = browser.current_window_handle
                while True:
                    if len(browser.window_handles) == 1:
                        break
                    for handle in browser.window_handles:
                        if handle != browser.current_window_handle:
                            browser.switch_to.window(handle)
                            f.write(browser.current_url + "\n")
                            browser.close()
                            browser.switch_to.window(old_windows_handle)
                            break
                # results.append(browser.current_url)
                time.sleep(1)
    except Exception as e:
        print(e)
        return False
    finally:
        browser.close()
    return results


if __name__ == '__main__':
    get_html(chrome_path="D:\software\chromedriver.exe", url="https://gkcx.eol.cn/lineschool?luqutype=1")
