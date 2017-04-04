#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from multiprocessing import Process
import os
def run_proc(name):
	print('Run child process %s (%s)'% (name,os.getpid()))

if __name__=='___main__':
	print('Parent process %s.'% os.getpid())
	p=Process(target=run_proc,args=('test',))
	print('Child process will start.')
	p.start()
	p.join()
	print('Child process end.')