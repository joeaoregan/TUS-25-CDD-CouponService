# datetime.date class methods

import datetime

# datetime.date.today() 
# # returns today's date as an object

this_date = datetime.date.today()
print(this_date) # 2025-11-08

random_date = datetime.date(2025, 10, 21)
print(random_date) # 2025-10-21

# datetime.date.fromisoformat(date_sting)
# returns a date object from a string in ISO format YYYY-MM-DD

april_fools_day = datetime.date.fromisoformat("2021-04-01")
print(april_fools_day) # 2021-04-01
afd = datetime.date(2021, 4, 1)
print(afd) # 2021-04-01



###

this_date = datetime.date.today()
print(this_date) # 2025-11-08
datetime.date(2025, 10, 21)

print(this_date.year) # 2025
print(this_date.month) # 11
print(this_date.day) # 8

april_fools_day = datetime.date.fromisoformat("2026-04-01")
print(april_fools_day) # 2026-04-01
datetime.date(2026, 4, 1)

# april_fools_day = datetime.date.fromisoformat("2026/04/01") # ValueError: Invalid isoformat string: '2026/05/01'

april_fools_day = datetime.date.fromisoformat("01/04/2026") # ValueError: Invalid isoformat string: '01/04/2026'
# Has to be in the format YYYY-MM-DD e.g. 2026-04-01
