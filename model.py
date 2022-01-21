# coding: utf-8
from sqlalchemy import Column
from sqlalchemy.dialects.mysql import VARCHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Test(Base):
    __tablename__ = 'test'

    main = Column(VARCHAR(255), primary_key=True, comment='主键')
