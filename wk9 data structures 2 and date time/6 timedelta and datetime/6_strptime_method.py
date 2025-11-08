# datetime.datetime
# class method strptime(datetime_string, format) returns a datetime object
# corresponding to datetime_string, parsed according to specified format

import datetime

mandela_free = datetime.datetime.strptime("16:14 February 11 1990", "%H:%M %B %d %Y")
print(mandela_free) # 1990-02-11 16:14:00


# If you are only interested in the date, leave out the time arguments:

halloween = datetime.datetime.strptime("31/10/2020", "%d/%m/%Y")
print(halloween) # 2020-10-31 00:00:00


###


halloween = datetime.datetime.strptime("31/10/2025", "%d/%m/%Y")
print(halloween) # 2025-10-31 00:00:00
print(type(halloween)) # <class 'datetime.datetime'>

# Halloween as a date object
halloween = datetime.datetime.strptime("31/10/2025", "%d/%m/%Y").date()
print(halloween) # 2025-10-31
print(type(halloween)) # <class 'datetime.date'>