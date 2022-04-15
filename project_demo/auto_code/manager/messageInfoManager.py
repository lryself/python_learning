from ..models.messageInfoModel import MessageInfo as _MessageInfo

from flask import current_app
from ..models import db
from ..utils.commons import fPrint_id_by_time, query_to_dict
from ..utils.response_code import *


class MessageInfoManager(_MessageInfo):
    @classmethod
    def add(cls, **kwargs):
        AutoID = kwargs.get('AutoID')
        messageID = kwargs.get('messageID')
        messageTitle = kwargs.get('messageTitle')
        messageText = kwargs.get('messageText')
        classID = kwargs.get('classID')
        recevierType = kwargs.get('recevierType')
        IsDelete = kwargs.get('IsDelete')
        CreateTime = kwargs.get('CreateTime')

        filter_list = []
        if AutoID:
            filter_list.append(cls.AutoID == AutoID)
        if messageID:
            filter_list.append(cls.messageID == messageID)
        if messageTitle:
            filter_list.append(cls.messageTitle == messageTitle)
        if messageText:
            filter_list.append(cls.messageText == messageText)
        if classID:
            filter_list.append(cls.classID == classID)
        if recevierType:
            filter_list.append(cls.recevierType == recevierType)
        if IsDelete:
            filter_list.append(cls.IsDelete == IsDelete)
        if CreateTime:
            filter_list.append(cls.CreateTime == CreateTime)

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
                AutoID=AutoID,
                messageID=messageID,
                messageTitle=messageTitle,
                messageText=messageText,
                classID=classID,
                recevierType=recevierType,
                IsDelete=IsDelete,
                CreateTime=CreateTime,
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
        AutoID = kwargs.get('AutoID')
        messageID = kwargs.get('messageID')
        messageTitle = kwargs.get('messageTitle')
        messageText = kwargs.get('messageText')
        classID = kwargs.get('classID')
        recevierType = kwargs.get('recevierType')
        IsDelete = kwargs.get('IsDelete')
        CreateTime = kwargs.get('CreateTime')

        filter_list = []
        if AutoID:
            filter_list.append(cls.AutoID == AutoID)
        if messageID:
            filter_list.append(cls.messageID == messageID)
        if messageTitle:
            filter_list.append(cls.messageTitle == messageTitle)
        if messageText:
            filter_list.append(cls.messageText == messageText)
        if classID:
            filter_list.append(cls.classID == classID)
        if recevierType:
            filter_list.append(cls.recevierType == recevierType)
        if IsDelete:
            filter_list.append(cls.IsDelete == IsDelete)
        if CreateTime:
            filter_list.append(cls.CreateTime == CreateTime)

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
        AutoID = kwargs.get('AutoID')
        messageID = kwargs.get('messageID')
        messageTitle = kwargs.get('messageTitle')
        messageText = kwargs.get('messageText')
        classID = kwargs.get('classID')
        recevierType = kwargs.get('recevierType')
        IsDelete = kwargs.get('IsDelete')
        CreateTime = kwargs.get('CreateTime')


        filter_list = []
        if AutoID:
            filter_list.append(cls.AutoID == AutoID)
        if messageID:
            filter_list.append(cls.messageID == messageID)
        if messageTitle:
            filter_list.append(cls.messageTitle == messageTitle)
        if messageText:
            filter_list.append(cls.messageText == messageText)
        if classID:
            filter_list.append(cls.classID == classID)
        if recevierType:
            filter_list.append(cls.recevierType == recevierType)
        if IsDelete:
            filter_list.append(cls.IsDelete == IsDelete)
        if CreateTime:
            filter_list.append(cls.CreateTime == CreateTime)

        try:
            result_model = db.session.query(cls).filter(*filter_list)
        except Exception as e:
            current_app.logger.error(e)
            return code_db_error(e)

        if not result_model.first():
            return code_none_data()

        args = {}
        if AutoID:
            args['AutoID'] = AutoID
        if messageID:
            args['messageID'] = messageID
        if messageTitle:
            args['messageTitle'] = messageTitle
        if messageText:
            args['messageText'] = messageText
        if classID:
            args['classID'] = classID
        if recevierType:
            args['recevierType'] = recevierType
        if IsDelete:
            args['IsDelete'] = IsDelete
        if CreateTime:
            args['CreateTime'] = CreateTime

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
        AutoID = kwargs.get('AutoID')
        messageID = kwargs.get('messageID')
        messageTitle = kwargs.get('messageTitle')
        messageText = kwargs.get('messageText')
        classID = kwargs.get('classID')
        recevierType = kwargs.get('recevierType')
        IsDelete = kwargs.get('IsDelete')
        CreateTime = kwargs.get('CreateTime')

        filter_list = []
        if AutoID:
            filter_list.append(cls.AutoID == AutoID)
        if messageID:
            filter_list.append(cls.messageID == messageID)
        if messageTitle:
            filter_list.append(cls.messageTitle == messageTitle)
        if messageText:
            filter_list.append(cls.messageText == messageText)
        if classID:
            filter_list.append(cls.classID == classID)
        if recevierType:
            filter_list.append(cls.recevierType == recevierType)
        if IsDelete:
            filter_list.append(cls.IsDelete == IsDelete)
        if CreateTime:
            filter_list.append(cls.CreateTime == CreateTime)

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
        AutoID = kwargs.get('AutoID')
        messageID = kwargs.get('messageID')
        messageTitle = kwargs.get('messageTitle')
        messageText = kwargs.get('messageText')
        classID = kwargs.get('classID')
        recevierType = kwargs.get('recevierType')
        IsDelete = kwargs.get('IsDelete')
        CreateTime = kwargs.get('CreateTime')

        filter_list = []
        if AutoID:
            filter_list.append(cls.AutoID == AutoID)
        if messageID:
            filter_list.append(cls.messageID == messageID)
        if messageTitle:
            filter_list.append(cls.messageTitle == messageTitle)
        if messageText:
            filter_list.append(cls.messageText == messageText)
        if classID:
            filter_list.append(cls.classID == classID)
        if recevierType:
            filter_list.append(cls.recevierType == recevierType)
        if IsDelete:
            filter_list.append(cls.IsDelete == IsDelete)
        if CreateTime:
            filter_list.append(cls.CreateTime == CreateTime)

        try:
            result_model = db.session.query(cls).filter(*filter_list)
        except Exception as e:
            current_app.logger.error(e)
            return code_db_error(e)

        if not result_model.first():
            return code_none_data()

        result = query_to_dict(result_model.all())
        return code_ok(data=result)
