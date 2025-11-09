# datetime.date instance methods
# .strftime(format)

# returns a string representign the date, specified by a format string

# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes

import datetime

this_date = datetime.date.today()
print(this_date) # 2025-11-08

print(this_date.strftime('%d/%m/%Y')) # 08/11/2025
print(this_date.strftime('%A %d %b %Y')) # Saturday 08 Nov 2025


###


this_date = datetime.date.today()
this_date_next_year = this_date.replace(year=2026)

print(this_date_next_year.strftime("%d/%m/%y")) # 08/11/26
print(this_date_next_year.strftime("%d/%m/%Y")) # 08/11/2026
print(this_date_next_year.strftime("%A %d %B %Y")) # Sunday 08 November 2026
print(this_date_next_year.strftime("%a %d %b %y")) # Sun 08 Nov 26