#!/usr/bin/env python3
# -*- coding: utf-8 _8_

class Student(object):
	def __init__(self,name):
		self.name=name

	def __call__(self):
		print('My name is %s.' % self.name)

s=Student('huaihaizhi')
s()