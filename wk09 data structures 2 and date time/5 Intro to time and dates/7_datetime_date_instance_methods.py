# datetime.date instance methods

# .isoformat()

# returns a string representing the date
# in ISO format YYYY-MM-DD

import datetime

may_day = datetime.date(2021, 5, 1)
print(may_day) # 2021-05-01

print(may_day.isoformat()) # 2021-05-01

# .replace()

# returns a date object with the specified values replaced
fires_date = datetime.date(1998, 1, 1)
print(fires_date) # 1998-01-01
print(datetime.date(1998, 1, 1)) # 1998-01-01

correct_fires_date = fires_date.replace(month=2)
print(correct_fires_date) # 1998-02-01
print(datetime.date(1998, 2, 1)) # 1998-02-01

new_fires_date = fires_date.replace(month=2, day=20)
print(new_fires_date) # 1998-02-20
print(datetime.date(1998, 2, 20)) # 1998-02-20


###

this_date = datetime.date.today()
print(this_date) # 2025-11-08

print(this_date.isoformat()) # 2025-11-08


this_date.replace(year=2026)
print(this_date) # 2025-11-08

this_date_next_year = this_date.replace(year=2026)
print(this_date_next_year) # 2026-11-08