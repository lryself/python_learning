# coding: utf-8
# @Author : lryself
# @Date : 2022/2/16 23:16
# @Software: PyCharm
import time

from selenium import webdriver


def main(html_url):
    option = webdriver.ChromeOptions()
    # option.add_argument('headless')
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    option.add_experimental_option('useAutomationExtension', False)
    browser = webdriver.Chrome(executable_path="D:\download\chromedriver.exe", options=option)
    browser.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument',
                            {'source': 'Object.defineProperty(navigator, "webdriver", {get: () =>undefined})'})

    browser.maximize_window()
    browser.get(html_url)

    for i in range(1, 48):
        flag_text = browser.find_element_by_xpath(f'//*[@id="right"]/div[6]/table/tbody/tr[{i}]/td[7]/font').text
        if flag_text == "已完成":
            continue
        browser.find_element_by_xpath(f'//*[@id="right"]/div[6]/table/tbody/tr[{i}]/td[5]/a').click()
        while flag_text == "已完成":
            browser.refresh()
            flag_text = browser.find_element_by_xpath(f'//*[@id="right"]/div[6]/table/tbody/tr[{i}]/td[7]/font').text
            time.sleep(60)


if __name__ == '__main__':
    main("https://edu.nxgbjy.org.cn/student/clazz!main.action?clazz.id=241")
