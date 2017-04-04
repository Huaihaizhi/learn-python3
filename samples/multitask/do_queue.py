#!/usr/bin/env python
# -*- coding: utf-8 -*-
from multiprocessing import Process,Queue
import os,time,random
#写数据进程的代码
def write(q):
	print('Process to write:%s' % os.getpid())
	for value in ['A','B','C']:
		print('Put %s to queue...' % value)
		q.put(value)
		time.sleep(random.random())
#读数据进程的代码
def read(q):
	print('Process to read:%s' % os.getpid())
	while True:
		value=q.get(True)
		print('Get %s from queue.' % value)

if __name__=='__main__':
	#父进程创建Queue，并传给各个子进程
	q=Queue()
	pw=Process(target=write,args=(q,))
	pr=Process(target=read,args=(q,))
	#启动子程序pw，写入
	pw.start()
	#启用子程序pr，读取
	pr.start()
	#等待pw结束
	pw.join()
	#pr进程是死循环，无法等待其结束，只能强行终止：
	pr.terminate()