# time.gmtime(seconds)
# Returns UTC time corresponding to seconds since Epoch

import time

time.gmtime(1761054780)
# time.struct_time(tm_year=2025, tm_mon=11, tm_mday=8, tm_hour=18, tm_min=55, tm_sec=0, tm_wday=6,tm_yday=311, tm_isdst=0) # TypeError: structseq() takes at most 2 keyword arguments (9 given)
print(time.gmtime(1761054780)) # time.struct_time(tm_year=2025, tm_mon=10, tm_mday=21, tm_hour=13, tm_min=53, tm_sec=0, tm_wday=1, tm_yday=294, tm_isdst=0)

# By default returns current UTC time
time.gmtime()
# time.struct_time(tm_year=2025, tm_mon=11, tm_mday=8, tm_hour=18, tm_min=58, tm_sec=00, tm_wday=6,tm_yday=311, tm_isdst=0) # TypeError: structseq() takes at most 2 keyword arguments (9 given)
print(time.gmtime()) # time.struct_time(tm_year=2025, tm_mon=11, tm_mday=8, tm_hour=19, tm_min=0, tm_sec=11, tm_wday=5, tm_yday=312, tm_isdst=0) 


# time.gmtime(seconds=0)
# Returns UTC time corresponding to the Epoch

print(time.gmtime(0)) # time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=1, tm_isdst=0) -- Unix Epoch Time

# This system is using the UNIX Epoch, 00:00:00 UTC on the 1st of January 1970.


# time.localtime(seconds)
# by default returns current local time (system's timezone)

print(time.localtime()) # time.struct_time(tm_year=2025, tm_mon=11, tm_mday=8, tm_hour=19, tm_min=2, tm_sec=41, tm_wday=5, tm_yday=312, tm_isdst=0)

# tim_isdst=1 means Daylight Savings Time is in effect

# International Organisation for Standardisation (ISO)
# format: YYYY-MM-DD HH:MM:SS