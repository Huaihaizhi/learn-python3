#!/usr/bin python3
import mysql.connector

conn=mysql.connector.connect(user='root',password='',database='test')
cursor=conn.cursor()

sql="insert into employee(\
	first_name,last_name,age,sex,income) values ('%s','%s',%d,'%s',%d)" % ('Mac','Mohan',20,'M',12000)
try:
	cursor.execute(sql)
	conn.commit()
except:
	conn.rollback()
conn.close()