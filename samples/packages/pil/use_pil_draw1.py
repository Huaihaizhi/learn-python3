#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from PIL import Image,ImageDraw,ImageFont,ImageFilter
import random
def rndChar():
    return chr(random.randint(65,90))#根据随机ascii码，返回对应字符
def rndColor():
    return (random.randint(64,255),random.randint(64,255),random.randint(64,255))#返回随机颜色
def rndColor2():
    return (random.randint(32,127),random.randint(32,127),random.randint(32,127))
def line():
    return (random.random()*240,random.random()*60,random.random()*240,random.random()*60)#返回一个随机tuple
img=Image.new('RGBA',(240,60),(255,255,255))#创建图片，尺寸240x60，颜色模式RGB，填充色纯白色
font=ImageFont.truetype('C://Windows/Fonts/Arial.ttf',36)#设置字体的类型，font-family和font-size
draw=ImageDraw.Draw(img)#新建一个画板实例，传入参数刚刚创建的img对象作为画板
for x in range(0,img.size[0],2):#画板添加杂色
    for y in range(0,img.size[1]):
        draw.point((x,y),fill=rndColor())
for i in range(4):
    img1=Image.new('RGBA',(55,55),(255,255,255,0))#新建一个透明图片img1
    img_font=ImageDraw.Draw(img1)#img1作为画板
    img_font.text((15,8),rndChar(),font=font,fill=rndColor2())#img1上写字
    img1=img1.rotate(random.randint(-30,30))#img1旋转
    img.paste(img1,(10+i*60,10),mask=img1)#把img1粘贴到img上面
draw.line(line(),rndColor2())#添加干扰杂线
draw.line(line(),rndColor2())
draw.line(line(),rndColor2())
draw.line(line(),rndColor2())
img.show()#预览img
img.save('de.jpg','jpeg')