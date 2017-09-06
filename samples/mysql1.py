#!/usr/bin python3
import mysql.connector

conn=mysql.connector.connect(user='root',password='',database='test')

cursor=conn.cursor()
cursor.execute('drop table if exists employee')
sql='''
	create table employee (
	first_name char(20) not null,
	last_name char(20),
	age int,
	sex char(1),
	income float
	)
'''
try:
	cursor.execute(sql)
except:
	conn.rollback()
conn.close()