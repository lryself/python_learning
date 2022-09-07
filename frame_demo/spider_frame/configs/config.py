# coding: utf-8
# @Author : lryself
# @Date : 2022/7/31 10:52
# @Software: PyCharm

import os


"""配置信息"""
SECRET_KEY = "sadfjnklsahjfd1354asdas"

# 数据库连接配置
DIALECT = 'mysql'
DRIVER = 'mysqldb'
USERNAME = 'root'
PASSWORD = 'idealwifi@2020'
HOST = '115.29.137.201'
PORT = '13306'
DATABASE = 'webspider'
SQLALCHEMY_DATABASE_URI = '{}+{}://{}:{}@{}:{}/{}?charset=utf8'.format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST,
                                                                       PORT, DATABASE)

# 数据库连接快速手写数据库配置
# SQLALCHEMY_DATABASE_URI = "mysql+mysqldb://root:idealwifi@2020@115.29.137.201:13306/webspider?charset=utf8"

SQLALCHEMY_TRACK_MODIFICATIONS = True

# 数据库池的大小。 默认与数据库引擎的值相同 (通常为 5)
SQLALCHEMY_POOL_SIZE = 50

# 控制连接池达到最大大小后还可以创建的连接数，当这些附加连接返回到连接池时，它们将会被断开并丢弃。
SQLALCHEMY_MAX_OVERFLOW = 10

# token的有效期,单位：秒
TOKEN_EXPIRES = 3600

# 图片验证码的redis有效期, 单位：秒
IMAGE_CODE_REDIS_EXPIRES = 180

'''
  爬虫程序相关的常用参数配置
'''
#Base_URL地址 需要拼接网址时，配置基础URL地址
Base_URL = 'http://baidu.com'

# 代理池地址
PORXY_POOL_URL = 'http://139.9.128.8:5555/random'

#爬虫程序处理记录数范围--如果需要的时候使用
DATA_SPIDER_START = 1000000
DATA_SPIDER_END = 2000000

# JS引擎Splash服务器地址；
SPLASH_URL = 'http://10.21.32.1:8050/'

# Splash服务名称(用于监听脚本重启)
SPLASH_NAME = 'awesome_wescoff'

# 资源(页面)尝试获取访问次数
Access_Request_TIMES = 3

# 爬虫等待时间(秒)
WAITE_TIME = 10

# 临时文件夹路径
TEMP_DIR = "E:\\tempfile\\"

# 文件下载路径
DOWNLOAD_FILE_DIR = "E:\\downloadfiles\\"

# 数据库读取记录--每页的条数
PAGE_SIZE = 1000

# 默认创建进程数
PROCESS_SIZE = 4

# 默认日志格式
DEFAULT_LOG_FMT = '%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s: %(message)s'
# 默认时间格式
DEFUALT_LOG_DATEFMT = '%Y-%m-%d %H:%M:%S'
# 输出日志路径
LOG_OUT_PATH = os.path.join(os.path.dirname(__file__), 'logs', 'log')

# selenium默认driver路径
SELENIUM_DEFAULT_PATH = 'D:\python\wendriver\chromedriver.exe'
