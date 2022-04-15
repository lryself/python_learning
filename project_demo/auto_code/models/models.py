# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, ForeignKey, Index, Integer, LargeBinary, String
from sqlalchemy.schema import FetchedValue
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



class ClassAccount(db.Model):
    __tablename__ = 'class_account'

    AutoID = db.Column(db.BigInteger, primary_key=True, info='自动编号')
    ClassID = db.Column(db.ForeignKey('class_info.ClassID', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True, server_default=db.FetchedValue(), info='班级id')
    QuestionAccountID = db.Column(db.String(20, 'utf8_general_ci'), nullable=False, index=True, info='问题批次（这属于哪一次的作业）')
    QuestionAccountName = db.Column(db.String(20, 'utf8_general_ci'), nullable=False, info='问题编号')
    IsDelete = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='0-未删除，1-删除')
    Createtime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='创建时间')

    class_info = db.relationship('ClassInfo', primaryjoin='ClassAccount.ClassID == ClassInfo.ClassID', backref='class_accounts')



class ClassApply(db.Model):
    __tablename__ = 'class_apply'

    AutoID = db.Column(db.BigInteger, primary_key=True, info='自动编号')
    ClassID = db.Column(db.String(20, 'utf8_general_ci'), nullable=False, info='班级编号')
    StudentID = db.Column(db.String(20, 'utf8_general_ci'), nullable=False, info='学生ID')
    Status = db.Column(db.String(20, 'utf8_general_ci'), nullable=False, info='申请状态:\\r\\n0-退课未处理\\r\\n1-退课已处理')
    IsDelete = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='0-未删除，1-删除')
    Createtime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='创建时间')



class ClassInfo(db.Model):
    __tablename__ = 'class_info'

    AutoID = db.Column(db.BigInteger, primary_key=True, info='自动编号')
    ClassID = db.Column(db.String(20, 'utf8_general_ci'), nullable=False, index=True, server_default=db.FetchedValue(), info='班级id')
    SubjectID = db.Column(db.String(20, 'utf8_general_ci'), nullable=False, info='学科ID')
    ClassName = db.Column(db.String(255, 'utf8_general_ci'), nullable=False, info='班级名称')
    TeacherID = db.Column(db.String(20, 'utf8_general_ci'), nullable=False, info='老师id')
    UniversityID = db.Column(db.String(20, 'utf8_general_ci'), nullable=False, info='所属学校')
    IsDelete = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='0-未删除，1-删除')
    Createtime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='创建时间')



class ClassQuestion(db.Model):
    __tablename__ = 'class_question'

    AutoID = db.Column(db.BigInteger, primary_key=True, info='自动编号')
    ClassID = db.Column(db.ForeignKey('class_info.ClassID', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True, info='班级编号')
    QuestionID = db.Column(db.ForeignKey('question_info.QuestionID', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True, info='问题编号')
    QuestionAccountID = db.Column(db.ForeignKey('class_account.QuestionAccountID', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True, info='问题批次（这属于哪一次的作业）')
    IsDelete = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='0-未删除，1-删除')
    Createtime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='创建时间')

    class_info = db.relationship('ClassInfo', primaryjoin='ClassQuestion.ClassID == ClassInfo.ClassID', backref='class_questions')
    class_account = db.relationship('ClassAccount', primaryjoin='ClassQuestion.QuestionAccountID == ClassAccount.QuestionAccountID', backref='class_questions')
    question_info = db.relationship('QuestionInfo', primaryjoin='ClassQuestion.QuestionID == QuestionInfo.QuestionID', backref='class_questions')



class ClassStudent(db.Model):
    __tablename__ = 'class_student'

    AutoID = db.Column(db.BigInteger, primary_key=True, info='自动编号')
    ClassID = db.Column(db.String(20), nullable=False, info='班级编号')
    StudentID = db.Column(db.String(20), nullable=False, info='学生编号')
    StudentType = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='学生类型：\\r\\n0-普通学生\\r\\n1-旁听生')
    IsDelete = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='0-未删除，1-删除')
    Createtime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='创建时间')



class MessageInfo(db.Model):
    __tablename__ = 'message_info'

    AutoID = db.Column(db.Integer, primary_key=True, info='自动编号')
    messageID = db.Column(db.String(20), info='消息编号')
    messageTitle = db.Column(db.String(255), info='消息标题')
    messageText = db.Column(db.String, info='消息内容')
    classID = db.Column(db.String(20), info='所属班级')
    recevierType = db.Column(db.String(20), info='接收人类型')
    IsDelete = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='0-未删除1-删除')
    CreateTime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='创建时间')



class QuestionInfo(db.Model):
    __tablename__ = 'question_info'

    QuestionID = db.Column(db.String(20, 'utf8_general_ci'), primary_key=True, info='问题编号')
    SubjectID = db.Column(db.String(20, 'utf8_general_ci'), nullable=False, info='学科ID')
    QuestionText = db.Column(db.String(collation='utf8_general_ci'), nullable=False, info='问题内容')
    AnswerText = db.Column(db.String, nullable=False, info='答案内容')
    Createtime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='创建时间')



class SchoolInfo(db.Model):
    __tablename__ = 'school_info'

    UniversityID = db.Column(db.Integer, primary_key=True, info='学校编号')
    UniversityName = db.Column(db.String(255, 'utf8_general_ci'), nullable=False, server_default=db.FetchedValue(), info='学校名称')
    Createtime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='创建时间')



class StaticPhoto(db.Model):
    __tablename__ = 'static_photo'

    Auto = db.Column(db.Integer, primary_key=True, info='自动编号')
    photoID = db.Column(db.String(20), nullable=False, info='图片编号')
    photoUrl = db.Column(db.String(255), nullable=False, info='云储存图片网址')



class StudentQuestionAnswer(db.Model):
    __tablename__ = 'student_question_answer'

    AutoID = db.Column(db.BigInteger, primary_key=True, info='自动编号')
    StudentID = db.Column(db.String(20), nullable=False, info='学生编号')
    QuestionID = db.Column(db.String(20), nullable=False, info='问题编号')
    QuestionAccountID = db.Column(db.String(20), nullable=False, info='问题批次')
    AnswerText = db.Column(db.String, info='学生答案')
    IsReCheck = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='0-未复议\\r\\n1-申请复议，待老师处理\\r\\n2-复议完成，老师已处理')
    ImageUrl = db.Column(db.String(255, 'utf8_general_ci'), nullable=False, info='图片储存路径')
    Grade = db.Column(db.Integer, info='成绩')
    IsDelete = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='0-未删除，1-删除')
    Createtime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='创建时间')



class SubjectInfo(db.Model):
    __tablename__ = 'subject_info'

    SubjectID = db.Column(db.String(20, 'utf8_general_ci'), primary_key=True, info='学科ID')
    SubjectName = db.Column(db.String(255), info='学科名称')
    Createtime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='创建时间')



class SysSession(db.Model):
    __tablename__ = 'sys_session'

    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.String(255, 'utf8mb4_0900_ai_ci'), unique=True)
    data = db.Column(db.LargeBinary)
    expiry = db.Column(db.DateTime, server_default=db.FetchedValue())



class UserInfo(db.Model):
    __tablename__ = 'user_info'
    __table_args__ = (
        db.Index('NonClusteredIndex-学生基本信息索引', 'UserID', 'UserName', 'UniversityID'),
    )

    UserID = db.Column(db.String(30, 'utf8_general_ci'), primary_key=True, info='编号id')
    UserName = db.Column(db.String(30, 'utf8_general_ci'), nullable=False, info='姓名')
    UserNumber = db.Column(db.String(30, 'utf8_general_ci'), info='学号、员工号、教工号')
    Password = db.Column(db.String(255, 'utf8_general_ci'), nullable=False, info='密码')
    Email = db.Column(db.String(255, 'utf8_general_ci'), nullable=False, info='邮箱')
    UniversityID = db.Column(db.String(20, 'utf8_general_ci'), info='学校')
    UserType = db.Column(db.String(10), nullable=False, info='用户类型\\r\\n1--学生\\r\\n2--老师\\r\\n3--学校管理员\\r\\n4--平台管理员')
    Createtime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='创建时间')

class_dict = {key: var for key, var in locals().items() if isinstance(var, type)}
