# coding: utf-8
# @Author : lryself
# @Date : 2022/7/28 0:26
# @Software: PyCharm
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options

# 不加载图片,不缓存在硬盘(内存)
SERVICE_ARGS = ['--load-images=false', '--disk-cache=false']
chrome_options = Options()
chrome_options.add_argument("--headless")
# 创建浏览器, 添加参数设置为无界面浏览器
driver = webdriver.Chrome(service_args=SERVICE_ARGS, chrome_options=chrome_options)
# 设置等待时间
waite = WebDriverWait(driver, 5)
driver.get('https://taobao.com/')


def get_page_num():
    # 等待搜索框出现
    input_block = waite.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#q')))
    # 输入美食
    input_block.send_keys('美食')
    # 点击搜索
    driver.find_element_by_css_selector("#J_TSearchForm > div > button").click()
    # 共计多少页
    text = driver.find_element_by_css_selector('#mainsrp-pager > div > div > div > div[class="total"]').text
    data = text[2:6]
    get_product_info()
    return data


# 得到某一个宝贝,商品的大体信息
def get_product_info():
    waite.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-itemlist .items .item')))
    # 通过BeautifulSoup取数据
    soup = BeautifulSoup(driver.page_source, 'lxml')
    # 取所有的列表数据
    item_lists = soup.select("#mainsrp-itemlist .items .item")
    for item_list in item_lists:
        item_dict = {}
        image = item_list.select('.J_ItemPic.img')[0].attrs["data-src"]
        if not image:
            image = item_list.select('.J_ItemPic.img')[0].attrs["data-ks-lazyload"]
        # 销售地
        location = item_list.select(".location")[0].text
        # 价格
        price = item_list.select(".price")[0].text
        # 商店名称
        shopname = item_list.select(".shopname")[0].text.strip()
        # 宝贝名称
        title = item_list.select('a[class="J_ClickStat"]')[0].text.strip()
        # 链接
        data_link = item_list.select('a[class="J_ClickStat"]')[0].attrs["href"]

        item_dict["image"] = "https:" + image
        item_dict["location"] = location
        item_dict["shopname"] = shopname
        item_dict["title"] = title
        item_dict["data_link"] = "https:" + data_link
        item_dict["price"] = price
        print(item_dict)


# 切换下一页
def next_page(page):
    print("当前正在加载第%s页的数据--------" % page)
    try:
        input_block = waite.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div > input')))
        input_block.clear()  # 清空输入框
        # 页面框添加页码
        input_block.send_keys(page)
        # 找到确定按钮,点击确定
        driver.find_element_by_css_selector("#mainsrp-pager > div > div > div > div > span.btn.J_Submit").click()
        waite.until(EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, "#mainsrp-pager > div > div > div > ul.items > li.item.active"), str(page)))
    except Exception as e:
        print(e)
        next_page(page)
    # 当前切换后的页面的数据
    get_product_info()


def main():
    data = get_page_num()
    print('总页数是=', data)
    for page in range(2, int(data) + 1):
        next_page(page)

    # 退出浏览器
    driver.quit()


if __name__ == '__main__':
    main()