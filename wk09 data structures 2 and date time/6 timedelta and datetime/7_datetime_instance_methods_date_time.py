# datetime.datetime Instance Methods

# date() - Return date object with same year, month and day.
# time() - Return time object with same hour, minute, second, microsecond

import datetime

mandela_free = datetime.datetime.strptime("16:14 February 11 1990", "%H:%M %B %d %Y")
print(mandela_free) # 1990-02-11 16:14:00
print(mandela_free.date()) # 1990-02-11
print(mandela_free.time()) # 16:14:00

halloween = datetime.datetime.strptime("31/10/2025", "%d/%m/%Y")
print(halloween) # 2025-10-31 00:00:00
print(halloween.date()) # 2025-10-31


# isofomat() - Return a string representing the datetime in ISO format
# strftime(format) - Return a string representing datetime object, specified by a format string

this_moment = datetime.datetime.now()
print(this_moment) # 2025-11-08 21:27:43.340555s
print(this_moment.strftime("%I.%M %p %A %d %B %Y")) # 09.27 PM Saturday 08 November 2025
print(this_moment.isoformat()) # 2025-11-08T21:27:43.340555