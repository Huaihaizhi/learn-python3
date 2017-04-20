#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from PIL import Image,ImageFilter
im=Image.open('test.jpg')
im2=im.filter(ImageFilter.BLUR)
im2.save('sw.jpg','jpeg')