#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from contextlib import contextmanager
class Query(object):
	def __init__(self,name):
		self.nane=name

	def query(self):
		print('Query info about %s...' % self.name)

@contextmanager
def create_query(name):
	print('start')
	q=Query(name)
	yield q
	print('end')

with create_query('Bob') as q:
	q.query()