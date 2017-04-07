#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from datetime import datetime,timedelta,timezone

now=datetime.now()
print('now=',now)
print('type(now)=',type(now))

dt=datetime(2017,4,7,20,59)
print('dt=',dt)

print('datetime->timestamp:',dt.timestamp())

t=dt.timestamp()
print('timestamp->datetime',datetime.fromtimestamp(t))
print('timestamp->datetime as UTC-0',datetime.utcfromtimestamp(t))

cday=datetime.strptime('2017-4-7 21:04:00','%Y-%m-%d %H:%M:%S')
print('strptime:',cday)

print('current datetime=',cday)
print('current +10 hours=',cday-timedelta(hours=10))
print('current -1 day=',cday-timedelta(days=1))
print('current +2.5 days=',cday+timedelta(days=2,hours=12))

utc_dt=datetime.utcnow().replace(tzinfo=timezone.utc)
utc8_dt=utc_dt.astimezone(timezone(timedelta(hours=8)))
print('UTC+0:00 now=',utc_dt)
print('UTC+8:00 now=',utc8_dt)