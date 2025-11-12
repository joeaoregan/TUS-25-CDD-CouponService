import datetime

print(datetime.datetime.now()) # 2025-11-08 21:01:36.707626

this_moment = datetime.datetime.now()

halloween_night = datetime.datetime(2025, 10, 31, 23, 59, 59)
print(halloween_night) # 2025-10-31 23:59:59

difference = halloween_night - this_moment
print(difference) # -8 days, 2:57:34.148794
