#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from PIL import Image

im=Image.open('test.jpg')
w,h=im.size
print('Origin image size:%sx%s' % (w,h))

im.thumbnail((w//2,h//2))
im.save('aq.jpg','jpeg')