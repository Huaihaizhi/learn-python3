#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import pickle
d=dict(name='huaihaizhi',age=20,score=95)
data=pickle.dumps(d)
print(data)

reborn=pickle.loads(data)
print(reborn)