from ..models.studentQuestionAnswerModel import StudentQuestionAnswer as _StudentQuestionAnswer

from flask import current_app
from ..models import db
from ..utils.commons import fPrint_id_by_time, query_to_dict
from ..utils.response_code import *


class StudentQuestionAnswerManager(_StudentQuestionAnswer):
    @classmethod
    def add(cls, **kwargs):
        AutoID = kwargs.get('AutoID')
        StudentID = kwargs.get('StudentID')
        QuestionID = kwargs.get('QuestionID')
        QuestionAccountID = kwargs.get('QuestionAccountID')
        AnswerText = kwargs.get('AnswerText')
        IsReCheck = kwargs.get('IsReCheck')
        ImageUrl = kwargs.get('ImageUrl')
        Grade = kwargs.get('Grade')
        IsDelete = kwargs.get('IsDelete')
        Createtime = kwargs.get('Createtime')

        filter_list = []
        if AutoID:
            filter_list.append(cls.AutoID == AutoID)
        if StudentID:
            filter_list.append(cls.StudentID == StudentID)
        if QuestionID:
            filter_list.append(cls.QuestionID == QuestionID)
        if QuestionAccountID:
            filter_list.append(cls.QuestionAccountID == QuestionAccountID)
        if AnswerText:
            filter_list.append(cls.AnswerText == AnswerText)
        if IsReCheck:
            filter_list.append(cls.IsReCheck == IsReCheck)
        if ImageUrl:
            filter_list.append(cls.ImageUrl == ImageUrl)
        if Grade:
            filter_list.append(cls.Grade == Grade)
        if IsDelete:
            filter_list.append(cls.IsDelete == IsDelete)
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
                AutoID=AutoID,
                StudentID=StudentID,
                QuestionID=QuestionID,
                QuestionAccountID=QuestionAccountID,
                AnswerText=AnswerText,
                IsReCheck=IsReCheck,
                ImageUrl=ImageUrl,
                Grade=Grade,
                IsDelete=IsDelete,
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
        AutoID = kwargs.get('AutoID')
        StudentID = kwargs.get('StudentID')
        QuestionID = kwargs.get('QuestionID')
        QuestionAccountID = kwargs.get('QuestionAccountID')
        AnswerText = kwargs.get('AnswerText')
        IsReCheck = kwargs.get('IsReCheck')
        ImageUrl = kwargs.get('ImageUrl')
        Grade = kwargs.get('Grade')
        IsDelete = kwargs.get('IsDelete')
        Createtime = kwargs.get('Createtime')

        filter_list = []
        if AutoID:
            filter_list.append(cls.AutoID == AutoID)
        if StudentID:
            filter_list.append(cls.StudentID == StudentID)
        if QuestionID:
            filter_list.append(cls.QuestionID == QuestionID)
        if QuestionAccountID:
            filter_list.append(cls.QuestionAccountID == QuestionAccountID)
        if AnswerText:
            filter_list.append(cls.AnswerText == AnswerText)
        if IsReCheck:
            filter_list.append(cls.IsReCheck == IsReCheck)
        if ImageUrl:
            filter_list.append(cls.ImageUrl == ImageUrl)
        if Grade:
            filter_list.append(cls.Grade == Grade)
        if IsDelete:
            filter_list.append(cls.IsDelete == IsDelete)
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
        AutoID = kwargs.get('AutoID')
        StudentID = kwargs.get('StudentID')
        QuestionID = kwargs.get('QuestionID')
        QuestionAccountID = kwargs.get('QuestionAccountID')
        AnswerText = kwargs.get('AnswerText')
        IsReCheck = kwargs.get('IsReCheck')
        ImageUrl = kwargs.get('ImageUrl')
        Grade = kwargs.get('Grade')
        IsDelete = kwargs.get('IsDelete')
        Createtime = kwargs.get('Createtime')


        filter_list = []
        if AutoID:
            filter_list.append(cls.AutoID == AutoID)
        if StudentID:
            filter_list.append(cls.StudentID == StudentID)
        if QuestionID:
            filter_list.append(cls.QuestionID == QuestionID)
        if QuestionAccountID:
            filter_list.append(cls.QuestionAccountID == QuestionAccountID)
        if AnswerText:
            filter_list.append(cls.AnswerText == AnswerText)
        if IsReCheck:
            filter_list.append(cls.IsReCheck == IsReCheck)
        if ImageUrl:
            filter_list.append(cls.ImageUrl == ImageUrl)
        if Grade:
            filter_list.append(cls.Grade == Grade)
        if IsDelete:
            filter_list.append(cls.IsDelete == IsDelete)
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
        if AutoID:
            args['AutoID'] = AutoID
        if StudentID:
            args['StudentID'] = StudentID
        if QuestionID:
            args['QuestionID'] = QuestionID
        if QuestionAccountID:
            args['QuestionAccountID'] = QuestionAccountID
        if AnswerText:
            args['AnswerText'] = AnswerText
        if IsReCheck:
            args['IsReCheck'] = IsReCheck
        if ImageUrl:
            args['ImageUrl'] = ImageUrl
        if Grade:
            args['Grade'] = Grade
        if IsDelete:
            args['IsDelete'] = IsDelete
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
        AutoID = kwargs.get('AutoID')
        StudentID = kwargs.get('StudentID')
        QuestionID = kwargs.get('QuestionID')
        QuestionAccountID = kwargs.get('QuestionAccountID')
        AnswerText = kwargs.get('AnswerText')
        IsReCheck = kwargs.get('IsReCheck')
        ImageUrl = kwargs.get('ImageUrl')
        Grade = kwargs.get('Grade')
        IsDelete = kwargs.get('IsDelete')
        Createtime = kwargs.get('Createtime')

        filter_list = []
        if AutoID:
            filter_list.append(cls.AutoID == AutoID)
        if StudentID:
            filter_list.append(cls.StudentID == StudentID)
        if QuestionID:
            filter_list.append(cls.QuestionID == QuestionID)
        if QuestionAccountID:
            filter_list.append(cls.QuestionAccountID == QuestionAccountID)
        if AnswerText:
            filter_list.append(cls.AnswerText == AnswerText)
        if IsReCheck:
            filter_list.append(cls.IsReCheck == IsReCheck)
        if ImageUrl:
            filter_list.append(cls.ImageUrl == ImageUrl)
        if Grade:
            filter_list.append(cls.Grade == Grade)
        if IsDelete:
            filter_list.append(cls.IsDelete == IsDelete)
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
        AutoID = kwargs.get('AutoID')
        StudentID = kwargs.get('StudentID')
        QuestionID = kwargs.get('QuestionID')
        QuestionAccountID = kwargs.get('QuestionAccountID')
        AnswerText = kwargs.get('AnswerText')
        IsReCheck = kwargs.get('IsReCheck')
        ImageUrl = kwargs.get('ImageUrl')
        Grade = kwargs.get('Grade')
        IsDelete = kwargs.get('IsDelete')
        Createtime = kwargs.get('Createtime')

        filter_list = []
        if AutoID:
            filter_list.append(cls.AutoID == AutoID)
        if StudentID:
            filter_list.append(cls.StudentID == StudentID)
        if QuestionID:
            filter_list.append(cls.QuestionID == QuestionID)
        if QuestionAccountID:
            filter_list.append(cls.QuestionAccountID == QuestionAccountID)
        if AnswerText:
            filter_list.append(cls.AnswerText == AnswerText)
        if IsReCheck:
            filter_list.append(cls.IsReCheck == IsReCheck)
        if ImageUrl:
            filter_list.append(cls.ImageUrl == ImageUrl)
        if Grade:
            filter_list.append(cls.Grade == Grade)
        if IsDelete:
            filter_list.append(cls.IsDelete == IsDelete)
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
