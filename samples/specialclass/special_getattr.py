#!/usr/bin/env python3
# -*- coding: utf-8 _*_

class Student(object):
	def __init__(self):
		self.name='huaihaizhi'

	def __getattr__(self,attr):
		if attr=='score':
			return 95
		if attr=='age':
			return lambda: 20
		raise AttributeError('\'Student\' object has no attribute \'%\'' % attr)


s=Student()
print(s.name)
print(s.score)
print(s.age())
print(s.grade)