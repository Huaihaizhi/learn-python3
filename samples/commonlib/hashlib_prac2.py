#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import hashlib
db={}
def get_md5(password):
	md5=hashlib.md5()
	md5.update(password.encode('utf-8'))
	return md5.hexdigest()

def register(username,password):
	db[username]=get_md5(username+password+'the-Salt')
	return db[username]

def login(username,password):
	if db.get(username)==register(username,password):
		print('mach it!')
	else:
		print('no match!')

register('Machael','12345')
register('Bob','password')
register('Amy','loveyou')
print(db)
login('Amy','loveyou')