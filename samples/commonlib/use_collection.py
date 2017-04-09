#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from collections import namedtuple
Point=namedtuple('Point',['x','y'])
p=Point(1,2)
print(p.x,p.y)

from collections import deque
q=deque(['a','b','c'])
q.append('y')
q.appendleft('x')
print(q)

from collections import defaultdict
cd=defaultdict(lambda:'None')
cd['key']=1
print('cd[\'key\']=',cd['key'])
print('cd[\'key1\']=',cd['key1'])

from collections import Counter
c=Counter()
for i in 'colections':
	c[i]+=1

print(c)
