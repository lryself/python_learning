# here put the import lib
# @Time : 2020/7/8 18:08
# @Author : liruiyang
# @File : dict_re
# @Software: PyCharm
import requests
import re
re_dict = {
    "地址": r"[^<]+",
    "地址2": r">[^<^=]*[\u4e00-\u9fa5]{2,5}[市省]([\u4e00-\u9fa5]{1,4}[市])?[^<]+",
    "座机电话": r"电话 *[（）\(\)a-zA-Z\u4e00-\u9fa5]* *[:：] *((\(\d{2,3}-?\d{0,3}\))|(\d{3,4}-))?\d{7,8}",
    "手机电话": r"电话 *[（）\(\)a-zA-Z\u4e00-\u9fa5]* *[:：](13[0-9]|14[57]|15[0-9]|18[0-9])\d{8}",
    "网站": r"网站 *[（）\(\)a-zA-Z\u4e00-\u9fa5]* *[:：][a-zA-Z0-9][-a-zA-Z0-9]{0,62}(\.[a-zA-Z0-9][-a-zA-Z0-9]{0,62})+\.?",
    "邮箱": r"(Mail|邮箱) *[（）\(\)a-zA-Z\u4e00-\u9fa5]* *[:：]\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*",
    "邮编": r"邮编 *[（）\.\(\)a-zA-Z\u4e00-\u9fa5]* *[:：][1-9]\d{5}(?!\d)"
}

if __name__ == '__main__':
    # url = 'http://http://www.zkjskf.cn/index/lists/catid/31.html'
    url = 'http://www.chinadaheng.com.cn/aboutus_contactus.aspx'
    try:
        print("正在链接网址{}".format(url))
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
        response = requests.get(url, headers=headers, timeout=5).content.decode("utf-8")
    except:
        print("{}链接失败".format(url))
    else:
        print(re.findall(re_dict.get("地址2"), response))
        # print(re.findall(re_dict.get("座机电话"), response))