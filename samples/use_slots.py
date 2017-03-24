#!/usr/bin/env python3
# -*- coding utf-8 -*-

class Student(object):
	__slots__=('name','age')

class GraduateStudent(Student):
	pass


s=Student()
s.name='huaihaizhi'
s.age=20

try:
	s.score=100
except AttributeError as e:
	print('AttributeError:',e)


g=GraduateStudent()
g.score=95
print('g.score=',g.score)