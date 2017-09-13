#!/usr/bin/python3
import threading,time
exitFlag=0

def run(name,counter,delay):
	print('开始线程：'+name)
	while counter:
		if exitFlag:
			name.exit()
		time.sleep(delay)
		print('%s:%s' % (name,time.ctime(time.time())))
		counter-=1
	print('退出线程：'+name)

t1=threading.Thread(target=run,args=('t1',5,1))
t2=threading.Thread(target=run,args=('t2',5,2))
t1.start()
t2.start()
t1.join()
t2.join()
print('退出线程')