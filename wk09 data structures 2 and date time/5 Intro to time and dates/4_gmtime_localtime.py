#!/user/bin/env python3
# -*- coding: utf-8 -*-
"""
Examples of time functions
time.gmtime() - returns a time structure using UTC / GMT
time.localtime() - returns a time structure representing local time
"""

from time import gmtime, localtime

# gmtime returns the current UTC time as a structure
print(f"Current UTC time: {gmtime()}") # Current UTC time: time.struct_time(tm_year=2025, tm_mon=11, tm_mday=8, tm_hour=19, tm_min=8, tm_sec=42, tm_wday=5, tm_yday=312, tm_isdst=0)
# 0 seconds since the start of the Epoch
print(f"\nEpoch: {gmtime(0)}") # Epoch: time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=1, tm_isdst=0)

# gmtime returns the current local times as a time structure
print(f"\nCurrent local time: {localtime()}") # Current local time: time.struct_time(tm_year=2025, tm_mon=11, tm_mday=8, tm_hour=19, tm_min=8, tm_sec=42, tm_wday=5, tm_yday=312, tm_isdst=0)


###### DON'T USE FILENAMES SUCH AS time.py or datetime.py ######