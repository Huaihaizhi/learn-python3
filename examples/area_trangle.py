#!/usr/bin python3
a=float(input('输入三角形的第一条边长：'))
b=float(input('输入三角形的第二条边长：'))
c=float(input('输入三角形的第三条边长：'))

s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print('三角形的面积为：%0.2f' % area)