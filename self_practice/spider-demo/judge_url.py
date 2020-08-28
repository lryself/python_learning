# here put the import lib
# @Time : 2020/7/1 11:18
# @Author : liruiyang
# @File : judge_url
# @Software: PyCharm


import re

# 这个应该是在配置文件中的
WEBSITE_EXCLUDE = ['qq.com', 'weixin.com']


def judge_right_url(url):
    main_url = re.split('/|\?', url)
    for j in main_url:
        if re.match('^http.*', j):
            continue
        if j == '':
            continue
        if re.match(".*\.com$", j):
            for i in WEBSITE_EXCLUDE:
                res = re.match(".*{}$".format(i), j)
                if res:
                    return 1
    else:
        return 0


if __name__ == '__main__':
    url = "http://www.dong.weixin.com/index.com?name=李"
    print(judge_right_url(url))
