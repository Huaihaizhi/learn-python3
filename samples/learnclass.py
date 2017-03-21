#！/uer/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):
	def __init__(self,name,score):
		self.name = name
		self.score = score
	def print_score(self):
		print('%s:%s'%(self.name,self.score))
	def get_grade(self):
		if self.score>=90:
			return 'A'
		elif self.score>=60:
			return 'B'
		else:
			return 'C'


bart =  Student('bart',50)
lisa = Student('lisa',70)
jack = Student('jack',90)

print('bart.name=',bart.name)
print('bart.score=',bart.score)
bart.print_score

print('grade of bart:',bart.get_grade())
print('grade of jack:',jack.get_grade())