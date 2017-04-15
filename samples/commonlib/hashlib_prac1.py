#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import hashlib
db ={
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}
def calc_md5(password):
	md5=hashlib.md5()
	md5.update(password.encode())
	return md5.hexdigest()

def login(name,password):
	if db.get(name)==calc_md5(password):
		print('match it!')
	else:
		print('no match!')
login('michael','123456')