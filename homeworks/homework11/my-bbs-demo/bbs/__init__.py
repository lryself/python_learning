#!/usr/bin/python
# -*- coding: UTF-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import config

# 创建数据库连接引擎
engine = create_engine(config.SQLALCHEMY_DATABASE_URI, pool_size=config.POOL_SIZE, max_overflow=config.MAX_OVERFLOW)

# 创建DBSession类型--链接池
DBSession = sessionmaker(bind=engine)

# 创建Session--在连接池中取一个具体的实例
session = DBSession()
