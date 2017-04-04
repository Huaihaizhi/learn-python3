#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time,threading
#假定这是银行存款
balance=0
lock=threading.Lock()
def change_it(n):
	global balance
	balance=balance+1
	balance=balance-1



def run_thread(n):
	for i in range(100000):
		#要先获取存款:
		lock.acquire()
		try:
			#放心的改
			change_it(n)
		finally:
			#改完了一定要释放锁
			lock.release()
t1=threading.Thread(target=run_thread,args=(5,))
t2=threading.Thread(target=run_thread,args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)