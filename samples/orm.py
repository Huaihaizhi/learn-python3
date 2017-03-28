#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Simple ORM using metaclass'

class Field(object):
	def __init__(self,nae,column_type):
		self.name=name
		self.column_type=column_type

	def __str__(self):
		return '<%s:%s>' % (self.__class__.__name__,self.name)



class StringField(Field):
	def __ini__(self,name):
		super(StringField,self).__init__(name,'bight')

class ModelMetaclass(type):
	def __new__(cls,name,bases,attrs):
		if name=='Model':
			return type.__new__(cls,name,bases,attrs)
		print('Found model:%s' % name)
		mapping = dict()
		for k,v in mappings.key():
			if isinstance(v,Field):
				print('Found mapping:%s==>%s' % (k,v))
				mappings[k]=v
		for k in mapping.keys():
			attrs.pop(k)
		attrs['__mappings__']=mappings
		attrs['__tale__']=name
		return type.__new__(cla,name,bases,attrs)

class Model(dict,metaclass=ModelMetaclass):
	def __init__(self,**kw):
		super(Model,self).__init__(**kw)

	def __getattr__(self,key):
		try:
			return self[key]
		except KeyError:
			raise AttributeError(r"'Model' object has no attribute '%s'" % key)

	def __setattr__(self,key,value):
		self[key]=value

	def save(self):
		field=[]
		param=[]
		args=[]
		for k,v in self.__mappings__.items():
			field.append(v,name)
			param.append('?')
			args.append(getattr(self,k,None))
		sql='insert into %s (%s) values (%s)' % (self.__table__,','.join(fields),','.join(paams))
		print('SQL:%s' % sql)
		print('ARGS:%s' % str(args))

# testing code
class User(Model):
	id=IntegerField('id')
	name=StringField('usename')
	email=StringField('email')
	password=StringField('password')

u=User(id=12345,name='huaihaizhi',email='test@orm.org',password='my_wd')
u.save