#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import struct
def isBmp(file):
	with open(file,'rb') as fp:
		a=fp.read(30)
		stri=struct.unpack('<ccIIIIIIHH',a)
		if stri[0]==b'B' and stri[1]==b'M':
			print(stri[2],stri[9])
			print(stri)
		else:
			print('not bmp')
a='D://python3.6/test.jpg'
isBmp(a)
