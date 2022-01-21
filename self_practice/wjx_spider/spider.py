# coding: utf-8
# @Author : lryself
# @Date : 2021/12/21 17:41
# @Software: PyCharm
import datetime
import random
import time
import pyautogui

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC


def make_score_list(elm_num, max_num, min_num):
    while True:
        score_list = []
        r = 0
        for i in range(elm_num):
            q = random.randint(1, 5)
            r += q
            score_list.append(q)
        if max_num < r / elm_num < min_num:
            return score_list


def get_html(html_url):
    start = datetime.datetime.now()

    option = webdriver.ChromeOptions()
    # option.add_argument('headless')
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    option.add_experimental_option('useAutomationExtension', False)
    browser = webdriver.Chrome(executable_path="D:\download\chromedriver.exe", options=option)
    browser.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument',
                            {'source': 'Object.defineProperty(navigator, "webdriver", {get: () =>undefined})'})

    browser.maximize_window()
    # browser = webdriver.Chrome(executable_path=chrome_path)
    # 进入无头模式更换上列代码

    browser.get(html_url)
    # 性别
    browser.find_element_by_xpath(f'//*[@id="div1"]/div[2]/div[{random.randint(1, 2)}]/span/a').click()
    # 年龄段
    browser.find_element_by_xpath(f'//*[@id="div2"]/div[2]/div[{random.randint(1, 7)}]/span/a').click()
    # 学历
    browser.find_element_by_xpath(f'//*[@id="div3"]/div[2]/div[{random.randint(1, 6)}]/span/a').click()
    # 行业
    browser.find_element_by_xpath('//*[@id="div4"]/div[2]/div/span/span[1]/span/span[2]').click()
    # time.sleep(0.1)
    WebDriverWait(browser, 3).until(
        EC.presence_of_element_located((By.XPATH, f'//*[@id="select2-q4-results"]/li[{random.randint(1, 30)}]'))
    ).click()
    # browser.find_element_by_xpath(f'//*[@id="select2-q4-results"]/li[{random.randint(1, 30)}]').click()

    # 职业
    browser.find_element_by_xpath('//*[@id="div5"]/div[2]/div/span/span[1]/span/span[2]').click()
    # time.sleep(0.1)
    WebDriverWait(browser, 3).until(
        EC.presence_of_element_located((By.XPATH, f'//*[@id="select2-q5-results"]/li[{random.randint(1, 14)}]'))
    ).click()
    # browser.find_element_by_xpath(f'//*[@id="select2-q5-results"]/li[{random.randint(1, 14)}]').click()

    # 工作时长
    browser.find_element_by_xpath(f'//*[@id="div6"]/div[2]/div[{random.randint(1, 7)}]/span/a').click()

    # 情绪耗竭
    score_list = make_score_list(5, 2.5, 3)
    for i in range(5):
        browser.find_element_by_xpath(f'//*[@id="drv7_{i + 1}"]/td[{score_list[i]}]/a').click()
    # 工作投入
    score_list = make_score_list(5, 3, 3.5)
    for i in range(5):
        browser.find_element_by_xpath(f'//*[@id="drv8_{i + 1}"]/td[{score_list[i]}]/a').click()
    # 乐观程度
    score_list = make_score_list(10, 3, 4)
    for i in range(10):
        browser.find_element_by_xpath(f'//*[@id="drv9_{i + 1}"]/td[{score_list[i]}]/a').click()
    # 时间压力
    score_list = make_score_list(6, 2.6, 3)
    for i in range(6):
        browser.find_element_by_xpath(f'//*[@id="drv10_{i + 1}"]/td[{score_list[i]}]/a').click()
    # 时间压力调整
    score_list = make_score_list(8, 3.4, 4)
    for i in range(8):
        browser.find_element_by_xpath(f'//*[@id="drv11_{i + 1}"]/td[{score_list[i]}]/a').click()

    browser.find_element_by_xpath('//*[@id="ctlNext"]').click()
    while browser.current_url.find("https://www.wjx.cn/wjx/join/completemobile2.aspx") == -1:
        try:
            # 提交
            pos = pyautogui.locateOnScreen('pic/img2.png')
            if pos:
                browser.refresh()
                time.sleep(random.random())

                pyautogui.moveTo(random.randint(100, 400), random.randint(300, 800))
                pyautogui.moveTo(random.randint(100, 400), random.randint(300, 800), duration=random.random()*2+0.5)
                pyautogui.click()
                WebDriverWait(browser, 3).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="confirm_box"]/div[2]/div[3]/button[2]'))
                ).click()
            try:
                elem = WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="alert_box"]')))
                if elem:
                    if not elem.get_attribute('style') == 'display: none;':
                        browser.find_element_by_xpath('//*[@id="alert_box"]/div[2]/div[2]/button').click()
                    browser.find_element_by_xpath("//div[@id='captcha']").click()
                    continue

            except Exception as e:
                print(e)

            browser.find_element_by_xpath('//*[@id="ctlNext"]').click()
            # pos = pyautogui.locateOnScreen('pic/img2.png')
            # if pos:
            #     cc = pyautogui.center(pos)
            #     pyautogui.moveTo(cc[0], cc[1])
            #     time.sleep(0.5)
            #     pyautogui.dragRel(256, 0, duration=0.8)
            #     pyautogui.moveTo(cc[0], cc[1])
            #     pyautogui.dragRel(500, 0, duration=3)

        except Exception as e:
            print(e)
        time.sleep(random.random())
    browser.close()

    end = datetime.datetime.now()
    print(end - start)


if __name__ == '__main__':
    url = "https://www.wjx.cn/vm/h4JVawY.aspx?code=061yYOFa14LYjC0rkIFa1EHWon4yYOFF&state=sojump"

    # for i in range(20):
    #     get_html(chrome_path="D:\download\chromedriver.exe", html_url=url)

    for i in range(100):
        get_html(url)
    # pool = Pool(2)
    # for i in range(100):
    #     pool.apply_async(get_html, (url,))
    #
    # pool.close()
    # pool.join()
