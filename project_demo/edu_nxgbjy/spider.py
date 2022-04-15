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
    browser = webdriver.Chrome(executable_path="D:\software\chromedriver.exe", options=option)
    browser.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument',
                            {'source': 'Object.defineProperty(navigator, "webdriver", {get: () =>undefined})'})

    browser.maximize_window()
    browser.get(html_url)
    # 640102197303290316
    # ljg729KYL!
    browser.find_element_by_xpath(f'//*[@id="name"]').send_keys("xxx")
    browser.find_element_by_xpath(f'//*[@id="jpassword"]').send_keys("xxx")
    verifycode = input("请输入验证码！")
    browser.find_element_by_xpath(f'//*[@id="imgcode"]').send_keys(verifycode)
    browser.find_element_by_xpath(f'//*[@id="form"]/table/tbody/tr[5]/td/input').click()
    browser.find_element_by_xpath(f'//*[@id="right"]/div[4]/table[2]/tbody/tr[3]/td[8]/a[1]').click()
    for i in range(2, 48):
        flag_text = browser.find_element_by_xpath(f'//*[@id="right"]/div[6]/table/tbody/tr[{i}]/td[7]/font').text
        if flag_text == "已完成":
            continue
        browser.find_element_by_xpath(f'//*[@id="right"]/div[6]/table/tbody/tr[{i}]/td[5]/a').click()
        while flag_text != "已完成":
            time.sleep(60)
            browser.refresh()
            browser.refresh()
            browser.refresh()
            flag_text = browser.find_element_by_xpath(f'//*[@id="right"]/div[6]/table/tbody/tr[{i}]/td[7]/font').text


if __name__ == '__main__':
    try:
        main("https://edu.nxgbjy.org.cn/")
    except Exception as e:
        print(e)
