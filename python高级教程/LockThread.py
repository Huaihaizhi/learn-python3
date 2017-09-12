#!/usr/bin python3
import threading,time
lock=threading.Lock()
balance=0

def change_it(n):
	global balance
	balance=balance+n
	balance=balance-n

def run_thread(n):
	for i in range(1000000):
		lock.acquire()
		try:
			change_it(n)
		finally:
			lock.release()

t1=threading.Thread(target=run_thread,args=(8,))
t2=threading.Thread(target=run_thread,args=(5,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)