#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import itertools
natuals=itertools.count(1)
for i in natuals:
	print(i)
	if i>=100:
		break

aq=itertools.cycle('ABC')
t=10
for c in aq:
	print(c)
	t-=1
	if t==0:
		break