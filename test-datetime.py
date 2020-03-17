from datetime import datetime

now = str(datetime.now())
# print(now)
# print(t)
# print(datetime.datetime.date(t))
# print(datetime.datetime.time(t))
print(now)
print(now[0:10], now[11:13], '-', now[14:16], '-', now[17:19])
print(now[0:10] + '-' + now[11:13] + '-' + now[14:16] + '-' + now[17:19])
