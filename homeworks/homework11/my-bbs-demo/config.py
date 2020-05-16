#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 数据库连接定义
SQLALCHEMY_DATABASE_URI = "mysql+mysqldb://root:123456@localhost:3306/test?charset=utf8"

# 初始化连接池的容量
POOL_SIZE=5

# 连接池的最大溢出容量： 该容量+初始容量= 最大容量；  超出会堵塞等待，timeout默认值30秒
MAX_OVERFLOW = 10
