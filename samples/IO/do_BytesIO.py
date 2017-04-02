#!/usr/bin/env python3
# -*- coding:utf-8 -8-


#write to BytesIO:
from io import BytesIO
f=BytesIO()
f.write(b'hello')
f.write(b' ')
f.write(b'world')
print(f.getvalue())

#read from BytesIO:
data='春雨初生，春林初盛，春风十里，不如你！'.encode('utf-8')
f=BytesIO(data)
print(f.read())