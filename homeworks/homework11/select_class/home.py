# -*- encoding: utf-8 -*-
"""
@File : home
@Time : 2020/5/16 12:56
@Author : lryself
@Version : 1.0
@Contact : lnolvwe@163.com
"""
# here put the import lib
import sys
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from manager import app  # 这里导入的是flask项目的运行模块
if len(sys.argv) == 2:
　　port = sys.argv[1]
else:
　　port = 5000

http_server = HTTPServer(WSGIContainer(app))
http_server.listen(port)
IOLoop.instance().start()