#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

mail_host='smtp.sohu.com'
user='###@sohu.com'
password='###'

sender='###@sohu.com'
receiver='###@qq.com'

message='''
<p>python 邮件发送测试。。。</p>
<p><a href="http://www.runoob.com">这是一个链接！</a></p>
'''
msg=MIMEMultipart()
msg['from']=Header('菜鸟教程','utf-8')
msg['to']=Header('坏孩纸','utf-8')
msg['subject']=Header('python测试','utf-8')

msg.attach(MIMEText('这是测试python发送带附件的邮件！','plain','utf-8'))

#构造附件
att1=MIMEText(open('test.txt','rb').read(),'base64','utf-8')
att1['Content-Type']='application/octet-stream'
#filename可以任意写，写什么名字，邮件中显示什么名字
att1['Content-Disposition']='attachment;filename="huaihaizhi.txt"'
msg.attach(att1)

try:
	smtpobj=smtplib.SMTP(mail_host,25)
	smtpobj.login(user,password)
	smtpobj.sendmail(sender,receiver,msg.as_string())
	print('邮件发送成功！')
except smtplib.SMTPException:
	print('Error:无法发送邮件！')