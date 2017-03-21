# 利用蒙特卡洛方法计算pi的值
from random import random
from math import sqrt
from time import clock
DARTS=2^10
hits=0
clock()
for i in range(1,DARTS):
    x,y=random(),random()
    dist=sqrt(x**2+y**2)
    if dist <= 1.0:
        hits=hits+1
pi = 4*(hits/DARTS)
print('the value of pi is %s' % pi)
print('the time of scanning is %-5.5ss' % clock())
