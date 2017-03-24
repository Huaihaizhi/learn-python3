#!/usr/bin/env python3
# -*- coding: utf-8 _*_

class Student(object):
	def __init__(self,name):
		self.name=name

	def __str__(self):
		return 'Student object (name:%s)' % self.name

	__repr__=__str__


print(Student('huaihaizhi'))