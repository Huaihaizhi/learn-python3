#!/usr/bin/env python3
# -*- coding:utf-8 _*_

import mysql.connector
conn=mysql.connector.connect(user='root',password='shengfang1115',database='test')
cursor=conn.cursor()
cursor.execute('create table user3 (id varchar(20) primary key,name varchar(20))')
cursor.execute('insert into user (id,name) values (%s,%s)',('3','huaihaizhi'))
print('rowcount=',cursor.rowcount)
conn.commit()
cursor.close()

cursor=conn.cursor()
cursor.execute('select * from user where id = %s',('3',))
values=cursor.fetchall()
print(values)
cursor.close()
conn.close()