#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def fn(self,name='world'):
	print('hello')


Hello=type('Hello',(object,),dict(hello=fn))


h=Hello()
print('call h.hello():')
h.hello()
print('type(Hello)=',type(Hello))
print('type(h)=',type(h))