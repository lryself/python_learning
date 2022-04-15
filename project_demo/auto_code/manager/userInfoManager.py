from ..models.userInfoModel import UserInfo as _UserInfo

from flask import current_app
from ..models import db
from ..utils.commons import fPrint_id_by_time, query_to_dict
from ..utils.response_code import *


class UserInfoManager(_UserInfo):
    @classmethod
    def add(cls, **kwargs):
        UserID = kwargs.get('UserID')
        UserName = kwargs.get('UserName')
        UserNumber = kwargs.get('UserNumber')
        Password = kwargs.get('Password')
        Email = kwargs.get('Email')
        UniversityID = kwargs.get('UniversityID')
        UserType = kwargs.get('UserType')
        Createtime = kwargs.get('Createtime')

        filter_list = []
        if UserID:
            filter_list.append(cls.UserID == UserID)
        if UserName:
            filter_list.append(cls.UserName == UserName)
        if UserNumber:
            filter_list.append(cls.UserNumber == UserNumber)
        if Password:
            filter_list.append(cls.Password == Password)
        if Email:
            filter_list.append(cls.Email == Email)
        if UniversityID:
            filter_list.append(cls.UniversityID == UniversityID)
        if UserType:
            filter_list.append(cls.UserType == UserType)
        if Createtime:
            filter_list.append(cls.Createtime == Createtime)

        # 检查是否有重复的邮箱
        try:
            result_model = db.session.query(cls).filter(*filter_list)
        except Exception as e:
            current_app.logger.error(e)
            return code_db_error(e)

        if result_model.first():
            return code_has_data()

        new_id = fPrint_id_by_time()
        # 生成用户id 插入信息到表里
        try:
            NewModel = cls.__call__(
                UserID=UserID,
                UserName=UserName,
                UserNumber=UserNumber,
                Password=Password,
                Email=Email,
                UniversityID=UniversityID,
                UserType=UserType,
                Createtime=Createtime,
            )
            db.session.add(NewModel)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            current_app.logger.error(e)
            return code_db_error(e)

        return code_ok()

    @classmethod
    def delete(cls, **kwargs):
        UserID = kwargs.get('UserID')
        UserName = kwargs.get('UserName')
        UserNumber = kwargs.get('UserNumber')
        Password = kwargs.get('Password')
        Email = kwargs.get('Email')
        UniversityID = kwargs.get('UniversityID')
        UserType = kwargs.get('UserType')
        Createtime = kwargs.get('Createtime')

        filter_list = []
        if UserID:
            filter_list.append(cls.UserID == UserID)
        if UserName:
            filter_list.append(cls.UserName == UserName)
        if UserNumber:
            filter_list.append(cls.UserNumber == UserNumber)
        if Password:
            filter_list.append(cls.Password == Password)
        if Email:
            filter_list.append(cls.Email == Email)
        if UniversityID:
            filter_list.append(cls.UniversityID == UniversityID)
        if UserType:
            filter_list.append(cls.UserType == UserType)
        if Createtime:
            filter_list.append(cls.Createtime == Createtime)

        try:
            result_model = db.session.query(cls).filter(*filter_list)
        except Exception as e:
            current_app.logger.error(e)
            return code_db_error(e)

        if not result_model.first():
            return code_none_data()

        try:
            result_model.delete()
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            current_app.logger.error(e)
            return code_db_error(e)

        result = query_to_dict(result_model.first())
        return code_ok(data=result)

    @classmethod
    def update(cls, **kwargs):
        UserID = kwargs.get('UserID')
        UserName = kwargs.get('UserName')
        UserNumber = kwargs.get('UserNumber')
        Password = kwargs.get('Password')
        Email = kwargs.get('Email')
        UniversityID = kwargs.get('UniversityID')
        UserType = kwargs.get('UserType')
        Createtime = kwargs.get('Createtime')


        filter_list = []
        if UserID:
            filter_list.append(cls.UserID == UserID)
        if UserName:
            filter_list.append(cls.UserName == UserName)
        if UserNumber:
            filter_list.append(cls.UserNumber == UserNumber)
        if Password:
            filter_list.append(cls.Password == Password)
        if Email:
            filter_list.append(cls.Email == Email)
        if UniversityID:
            filter_list.append(cls.UniversityID == UniversityID)
        if UserType:
            filter_list.append(cls.UserType == UserType)
        if Createtime:
            filter_list.append(cls.Createtime == Createtime)

        try:
            result_model = db.session.query(cls).filter(*filter_list)
        except Exception as e:
            current_app.logger.error(e)
            return code_db_error(e)

        if not result_model.first():
            return code_none_data()

        args = {}
        if UserID:
            args['UserID'] = UserID
        if UserName:
            args['UserName'] = UserName
        if UserNumber:
            args['UserNumber'] = UserNumber
        if Password:
            args['Password'] = Password
        if Email:
            args['Email'] = Email
        if UniversityID:
            args['UniversityID'] = UniversityID
        if UserType:
            args['UserType'] = UserType
        if Createtime:
            args['Createtime'] = Createtime

        try:
            result_model.update(args)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            current_app.logger.error(e)
            return code_db_error(e)

        result = query_to_dict(result_model.first())
        return code_ok(data=result)

    @classmethod
    def get(cls, **kwargs):
        UserID = kwargs.get('UserID')
        UserName = kwargs.get('UserName')
        UserNumber = kwargs.get('UserNumber')
        Password = kwargs.get('Password')
        Email = kwargs.get('Email')
        UniversityID = kwargs.get('UniversityID')
        UserType = kwargs.get('UserType')
        Createtime = kwargs.get('Createtime')

        filter_list = []
        if UserID:
            filter_list.append(cls.UserID == UserID)
        if UserName:
            filter_list.append(cls.UserName == UserName)
        if UserNumber:
            filter_list.append(cls.UserNumber == UserNumber)
        if Password:
            filter_list.append(cls.Password == Password)
        if Email:
            filter_list.append(cls.Email == Email)
        if UniversityID:
            filter_list.append(cls.UniversityID == UniversityID)
        if UserType:
            filter_list.append(cls.UserType == UserType)
        if Createtime:
            filter_list.append(cls.Createtime == Createtime)

        try:
            result_model = db.session.query(cls).filter(*filter_list)
        except Exception as e:
            current_app.logger.error(e)
            return code_db_error(e)

        if not result_model.first():
            return code_none_data()

        result = query_to_dict(result_model.first())
        return code_ok(data=result)

    @classmethod
    def get_list(cls, **kwargs):
        UserID = kwargs.get('UserID')
        UserName = kwargs.get('UserName')
        UserNumber = kwargs.get('UserNumber')
        Password = kwargs.get('Password')
        Email = kwargs.get('Email')
        UniversityID = kwargs.get('UniversityID')
        UserType = kwargs.get('UserType')
        Createtime = kwargs.get('Createtime')

        filter_list = []
        if UserID:
            filter_list.append(cls.UserID == UserID)
        if UserName:
            filter_list.append(cls.UserName == UserName)
        if UserNumber:
            filter_list.append(cls.UserNumber == UserNumber)
        if Password:
            filter_list.append(cls.Password == Password)
        if Email:
            filter_list.append(cls.Email == Email)
        if UniversityID:
            filter_list.append(cls.UniversityID == UniversityID)
        if UserType:
            filter_list.append(cls.UserType == UserType)
        if Createtime:
            filter_list.append(cls.Createtime == Createtime)

        try:
            result_model = db.session.query(cls).filter(*filter_list)
        except Exception as e:
            current_app.logger.error(e)
            return code_db_error(e)

        if not result_model.first():
            return code_none_data()

        result = query_to_dict(result_model.all())
        return code_ok(data=result)
