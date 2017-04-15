#!/usr/bin/env python
# -*- coding: utf-8 -*-
from contextlib import closing
from urllib.request import urlopen
with closing(urlopen('https://www.python.org')) as page:
	for line in page:
		print(line)