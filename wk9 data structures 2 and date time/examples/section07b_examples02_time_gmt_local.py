#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Examples of time functions
time.gmtime() - returns a time structure using UTC/GMT
time.localtime() - returns a time structure representing local time
"""
from time import gmtime, localtime

# gmtime returns the current UTC time as a time structure
print(f"Current UTC time: {gmtime()}")
print(f"\nEpoch: {gmtime(0)}") # 0 seconds since the start of the Epoch

# gmtime returns the current local time as a time structure
print(f"\nCurrent local time: {localtime()}")


