# coding: utf-8
from sqlalchemy import Column, DateTime, text
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Guestbook(Base):
    __tablename__ = 'guestbook'

    id = Column(INTEGER(11), primary_key=True, comment='留言编号')
    contents = Column(VARCHAR(50), server_default=text("''"), comment='留言内容')
    people = Column(VARCHAR(10), server_default=text("''"), comment='留言人员')
    time = Column(DateTime, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"), comment='留言时间')
    is_delete = Column(INTEGER(11), server_default=text("'0'"), comment='删除为1，不删除为0')
