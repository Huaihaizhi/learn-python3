import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header

mail_host='smtp.sohu.com'
mail_user='xxx.com'
mail_pass='xxx'

sender='huaohaizhi'
receivers=['xxx@qq.com']


msgRoot=MIMEMultipart('related')
msgRoot['from']=Header('坏孩纸')
msgRoot['to']=Header('测试')
msgRoot['subject']=Header('Python SMTP 邮件测试','utf-8')

msgAlternative=MIMEMultipart('alternative')
msgRoot.attach(msgAlternative)

mail_msg='''
<p>Python 邮件发送测试。。。</p>
<p><a href='http://www.runoob.com'>菜鸟教程链接</a></p>
<p>图片演示：</p>
<p><img src='cid:image1'></p>
'''

msgAlternative.attach(MIMEText(mail_msg,'html','utf-8'))

fp=open('test.jpg','rb')
msgImage=MIMEImage(fp.read())

msgImage.add_header('Content-ID','<image1>')
msgRoot.attach(msgImage)

try:
	smtpObj=smtplib.SMTP()
	smtpObj.connect(mail_host,25)
	smtpObj.login(mail_user,mail_pass)
	smtpObj.sendmail(mail_user,receivers,msgRoot.as_string())
	print('邮件发送成功！')
except smtplib.SMTPException:
	print('无法发送邮件！')