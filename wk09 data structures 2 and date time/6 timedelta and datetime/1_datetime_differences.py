# datetime.timedelta: datetime differences
# Example: Number of Days until New Year's Day 2026

# Difference between 2 dates: seconds and microseconds are zero

import datetime

# get a date object representing today
this_date = datetime.date.today()
print(f"Today is {this_date.strftime('%A %d %B %Y')}") # Today is Saturday 08 November 2025

# create a date object for New Year's Day 2026
new_years_day = datetime.date(2026,1,1)
print(f"New Year's Day 2026 will be on a {new_years_day.strftime('%A')}") # New Year's Day 2026 will be on a Thursday

# calculate the difference between today and New Year's Day:
delta = new_years_day - this_date
print(f"Number of days until New Year's Day 2026: {delta.days}") # Number of days until New Year's Day 2026: 54

print(delta) # 54 days, 0:00:00
print(type(delta)) # <class 'datetime.timedelta'>