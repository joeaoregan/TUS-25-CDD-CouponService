# The datetime module

# Provides classes for working with dates and times
# date: represent a date, attributes: year, month, and day

# time: represents a time, independent of any particular day,
# Attributes: hour, minute, second, microsecond, and tzinfo

# datetime: combination of a date and a time. Attributes: year, month
# day, hour, minutes, seconds, microsecond, and tzinfo

# timedelta: A duration expressing the difference between two date, time,
# or datetime instances (objects) to microsecond resolution.


# datetime methods

# Module provides class methods and instance methods

# Class methods are called on the class itself
#   datetime.date.fromisoformat(date_string)

# Instance methods are called on an instance (object)
#   fires_date.replace(month=10)

# fires_date is an instance of the datetime.date class (a date object)


# Working with Dates: datetime.date

# Create a date object:
#    datetime.date(year, month, day)

import datetime

halloween = datetime.date(2025, 10, 31)
print(halloween)
print(datetime.date(2025, 10, 31))

print(halloween.year) # 2025
print(halloween.month) # 10
print(halloween.day) # 31

no_such_date = datetime.date(2025,2,29)
print(no_such_date) # ValueError: day is out of range for month