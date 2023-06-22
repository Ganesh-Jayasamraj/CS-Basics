# Date - Time

import time, calendar

ticks = time.time()
print(ticks)

localtime = time.asctime(time.localtime(time.time()))
print(localtime)

cal = calendar.month(2008, 1)
print(cal)