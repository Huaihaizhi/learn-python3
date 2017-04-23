#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import sqlite3
conn=sqlite3.connect('test.db')
cursor=conn.cursor()
cursor.execute('create table user3 (id varchar(20) primary key,name varchar(20))')
cursor.execute('insert into user (id,name) values (\'3\',\'Michael\')')
print('rowcount=',cursor.rowcount)
cursor.close()
conn.commit()
conn.close()


#查询
conn=sqlite3.connect('test.db')
cursor=conn.cursor()
cursor.execute('select * from user where id=?','3')
values=cursor.fetchall()
print(values)
cursor.close()
conn.close()