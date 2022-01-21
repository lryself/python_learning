# coding: utf-8
# @Author : lryself
# @Date : 2021/2/27 10:12
# @Software: PyCharm

from smtplib import SMTP_SSL
from email.header import Header
from email.mime.text import MIMEText

if __name__ == '__main__':
    # qq邮箱smtp服务器
    host_server = 'smtp.qq.com'
    # 发送方邮箱
    sender = 'lryself@qq.com'
    # 填入发送方邮箱的授权码
    passwd = 'ikebnpaydyobieih'
    # 收件人邮箱
    recivers = ['lryself@qq.com']

    title = "python邮件测试"  # 主题
    content = "这是我使用python smtplib及email模块发送的邮件"  # 正文
    email_text = MIMEText(content)
    email_text['Subject'] = title
    email_text['From'] = sender
    email_text['To'] = Header("接收者测试", 'utf-8')

    try:
        smtp = SMTP_SSL(host_server)
        # set_debuglevel()是用来调试的。参数值为1表示开启调试模式，参数值为0关闭调试模式
        smtp.set_debuglevel(1)
        smtp.ehlo(host_server)
        smtp.login(sender, passwd)

        smtp.sendmail(sender, recivers, email_text.as_string())
        print("发送成功")
    except Exception as e:
        print("发送失败")
    finally:
        smtp.quit()
