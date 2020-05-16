# coding: utf-8
from sqlalchemy import Column, DECIMAL, DateTime, Enum, String, text
from sqlalchemy.dialects.mysql import BIT, INTEGER, TINYINT, VARCHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Class(Base):
    __tablename__ = 'classes'

    id = Column(INTEGER(10), primary_key=True)
    name = Column(String(30), nullable=False)


class Guestbook(Base):
    __tablename__ = 'guestbook'

    id = Column(INTEGER(11), primary_key=True, comment='????')
    contents = Column(VARCHAR(50), server_default=text("''"), comment='????')
    people = Column(VARCHAR(10), server_default=text("''"), comment='????')
    time = Column(DateTime, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"), comment='????')
    is_delete = Column(INTEGER(11), server_default=text("'0'"), comment='???1?????0')


class Student(Base):
    __tablename__ = 'students'

    id = Column(INTEGER(10), primary_key=True)
    name = Column(String(20), server_default=text("''"))
    age = Column(TINYINT(3), server_default=text("'0'"))
    height = Column(DECIMAL(5, 2))
    gender = Column(Enum('?', '?', '??', '??'), server_default=text("'??'"))
    cls_id = Column(INTEGER(10), server_default=text("'0'"))
    is_delete = Column(BIT(1))
