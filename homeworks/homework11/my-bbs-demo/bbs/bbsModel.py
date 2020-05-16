#!/usr/bin/python
# -*- coding: UTF-8 -*-

from sqlalchemy import BigInteger, Column, DateTime, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import FetchedValue
from . import session

Base = declarative_base()
metadata = Base.metadata

class BBsModel(Base):
    __tablename__ = 'bbs'

    autoID = Column(BigInteger, primary_key=True)
    username = Column(String(255, 'utf8_general_ci'), info='留言者')
    content = Column(String(1000, 'utf8_general_ci'), info='留言内容')
    addTime = Column(DateTime, server_default=FetchedValue(), info='记录添加时间')

    @classmethod
    def add_bbs(cls,**kwargs):

        try:
            bbs=BBsModel(
                username=kwargs.get('username'),
                content=kwargs.get('content')
                )

            session.add(bbs)
            session.commit()  # 将数据提交到数据库

        except Exception as e:
            session.rollback()
            return {'code':'201','message':'数据异常！'}

        finally:
            session.close()
            return {'code': 200, 'message': 'OK!'}


    @classmethod
    def get_bbs(cls,**kwargs):
        pass







