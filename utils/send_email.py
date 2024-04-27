#coding=utf-8
"""
===========================
Author:杭州多测师_王sir
Time:2022-11-19 12:55
website:https://duoceshi.net
===========================
"""

import os
import smtplib
import zipfile
from email.mime.text import MIMEText  # 正文用
from email.header import Header  # 标题用
from email.utils import formataddr


class SendEmail:

    def __init__(self, attachment, dirpath, outFullName):
        self.attachment = attachment
        self.dirpath = dirpath
        self.outFullName = outFullName

    def run(self):
        send_user = "18617162994@163.com"  # 邮箱地址
        send_password = "GNRSAFGCSVGOJXOW"  # 163邮箱的smtp密码
        send_smtp = "smtp.163.com"  # 使用的邮箱smtp官方地址
        receiver = "18617162994@163.com"  # 收件箱地址
        # 发送的附件内容
        # msg = MIMEText('hh', 'base64', 'utf-8')  # 数据编码方式是utf-8
        msg = MIMEText(open(self.attachment, 'rb').read(), "base64", "utf-8")
        msg['Content-Type'] = 'application/octet-stream'
        msg["Content-Disposition"] = 'attachment; filename=' + self.attachment

        # 第一种发件人方式：
        msg['From'] = send_user  # 发件人，声明收到邮件的时候发件人显示用（11不能写中文）
        print(type(msg['From']))  # 是一个email的对象
        msg['Subject'] = Header(u'cms系统ui自动化测试报告', 'utf-8').encode()  # u一般用在中文字符串前面，防止因为源码储存格式问题
        msg['To'] = 'tree'+receiver  # 收件人的名字（随便取）

        # print(msg)  # 打印发送给接受的数据
        # print(type(msg))
        # 实例化一个邮箱
        smtp = smtplib.SMTP()
        smtp.connect(send_smtp, 25)  # 这是发送出去的邮箱的smtp的地址和默认端口
        smtp.login(send_user, send_password)  # 这是登录的账号和smtp密码，用于除了网页以外的客户端登录
        # 发送邮件，传入发送账号，接收账号，将from和to subject当做字符串传入
        smtp.sendmail(send_user, [receiver, ], msg.as_string())
        smtp.quit()  # 关闭连接

    def zip_dir(self):
        zip = zipfile.ZipFile(self.outFullName, "w", zipfile.ZIP_DEFLATED)
        for path, dirnames, filenames in os.walk(self.dirpath):
            # 去掉目标跟路径，只对目标文件夹下边的文件及文件夹进行压缩
            fpath = path.replace(self.dirpath, '')
            for filename in filenames:
                zip.write(os.path.join(path, filename), os.path.join(fpath, filename))
        zip.close()
        print('压缩成功')

# 调试尝试一下是否调通
# a = SendEmail('send_report.zip',r'send_report',r"send_report.zip")
# a.run()
# a.zip_dir()