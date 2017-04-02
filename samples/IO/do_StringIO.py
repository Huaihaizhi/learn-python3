#1/usr/bin/env python3
# -*- codiing:utf-8 -*-
from io import StringIO
#write to StringIO:
f=StringIO()
f.write('hello')
f.write(' ')
f.write('world')
print(f.getvalue())


# read from StringIO:
f=StringIO('春雨初生，\n春林初盛，\n春风十里，\n不如你！')
while True:
	s=f.readline()
	if s=='':
		break
	print(s.strip())