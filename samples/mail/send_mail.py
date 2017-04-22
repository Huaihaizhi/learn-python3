#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.header import Header
from email import encoders
from email.utils import parseaddr,formataddr

def _formataddr_(s):
	name,addr=parseaddr(s)
	return formataddr((Header(name,'utf-8').encode(),addr))

msg=MIMEMultipart()
from_addr=input('your addr:')
password=input('password:')
to_addr=input('to addr:')
smtp_server=input('SMPT server:')

msg['From']=_formataddr_('Python爱好者<%s>' % from_addr)
msg['To']=_formataddr_('管理员<%s>' % to_addr)
msg['Subject']=Header('来自SMTP的问候.....','utf-8').encode()

msg.attach(MIMEText('Hello huaihaizhi!','plain','utf-8'))

with open('d://python3.6/test.jpg','rb') as f:
	mime=MIMEBase('image','jpg',filename='test.jpg')
	mime.add_header('Connect-Disposition','attachment',fiename='test.jpg')
	mime.add_header('Connect-ID','<0>')
	mime.add_header('X-Attachment-ID','0')
	mime.set_payload(f.read())
	encoders.encode_base64(mime)
	msg.attach(mime)

import smtplib
server=smtplib.SMTP(smtp_server,25)
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()