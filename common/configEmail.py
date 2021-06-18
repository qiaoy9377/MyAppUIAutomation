'''
功能描述：实现自动查找最新的测试报告文件，以附件形式发送测试报告邮件的功能
实现逻辑：
    1-导包
    2-配置邮件参数
    3-组装邮件内容
    4-登录并发送邮件
'''
from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from common.readConfig import ReadConfig
import os

class ConfigEmail():

    def __init__(self):
        rc = ReadConfig()
        self.sender = rc.readConfig('email','sender')
        self.receiver = rc.readConfig('email', 'receiver')
        self.smtpserver = rc.readConfig('email', 'smtpserver')
        self.username = rc.readConfig('email', 'username')
        self.password = rc.readConfig('email', 'password')
        self.subject = rc.readConfig('email', 'subject')
        self.content = rc.readConfig('email', 'content')

    def __config(self,report):
        #获取报告路径
        report_path = os.path.dirname(os.path.dirname(__file__))+'/testReport/'
        send_report = report_path+report
        with open(send_report,'rb') as sr:
            report_body = sr.read()
            msg = MIMEMultipart()
            att = MIMEText(report_body,'plain','utf-8')
            att['Content-Type'] = 'application/octet-stream'
            att['Content-Disposition'] = f'attachment;filename={report}'
            msg.attach(att)
            msg.attach(MIMEText(self.content,'plain','utf-8'))
            msg['Subject'] = Header(self.subject,'utf-8')
            msg['From'] = self.sender
            msg['To'] = self.receiver
        return msg

    def sendEmail(self,report):
        msg = self.__config(report)
        try:
            se = SMTP()
            se.connect(self.smtpserver)
            se.login(self.username,self.password)
            se.sendmail(self.sender,str(self.receiver).split(','),msg.as_string())
        except Exception as error:
            print('邮件发送失败',error)
        else:
            print('邮件发送成功')
        finally:
            se.quit()

if __name__ == '__main__':
    ce = ConfigEmail()
    ce.sendEmail('1.html')
