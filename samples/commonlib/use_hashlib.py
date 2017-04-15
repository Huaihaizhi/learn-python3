#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import hashlib
md5=hashlib.md5()
md5.update('how to learn hashlib in python?'.encode('utf-8'))
print(md5.hexdigest())


sha1=hashlib.sha1()
sha1.update('how to learn hashlib in '.encode('utf-8'))
sha1.update('python?'.encode('utf-8'))
print(sha1.hexdigest())
