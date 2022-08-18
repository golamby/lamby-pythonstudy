import time

# 1.时间戳
print(time.time())

# 2.格式化时间，2022-8-11 13:01:03 %Y-%m-%d %H:%M:%S
print(time.strftime('%Y-%m-%d %H:%M:%S %A'))
print(time.strftime('%Y-%m-%d %X %A'))
print(time.strftime('%x %X %A'))

# 3.结构化时间
print(time.localtime())
# time.struct_time(tm_year=2022, tm_mon=8, tm_mday=11, tm_hour=13, tm_min=52, tm_sec=31, tm_wday=3, tm_yday=223, tm_isdst=0)


import datetime

res = datetime.datetime.now()
print(res.replace(microsecond=0))

# time模块适合时间间隔的计算和时间格式化转换

res = datetime.datetime.now() + datetime.timedelta(days=25)
print(res)

# 时间戳--localtime()/gmtime()-->结构化时间--strftime-->格式化字符串时间
print('*' * 50)
res = time.time()  # 时间戳

print(time.localtime(res))  # 结构化时间
print(time.gmtime(res))

res = time.localtime(111111111)
print(time.strftime('%Y-%m-%d %X', res))  # 格式化字符串时间，第二个默认参数是time.localtime()

# 时间戳--localtime()/gmtime()-->结构化时间<--strptime--格式化字符串时间
t = '1973-07-10 08:11:51'
res = time.strptime(t, '%Y-%m-%d %X')
print(res)
print(time.mktime(res))

# time.sleep()

print(time.asctime())
print(time.ctime(time.time()))

print(datetime.datetime.now())
print(datetime.datetime.utcnow())

print(datetime.datetime.fromtimestamp(time.time()))
