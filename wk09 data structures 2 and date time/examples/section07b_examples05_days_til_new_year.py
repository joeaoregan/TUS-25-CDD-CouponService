#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Program to calculate the number of days until New Year's Day 2021
Example of datetime module: date and timedelta

@author: cormac
"""
import datetime

# get a date object representing today
this_date = datetime.date.today()
print(f"Today is {this_date.strftime('%A %d %B %Y')}")

# create a date object for New Year's Day 2026
new_years_day = datetime.date(2026,1,1)
print(f"New Year's Day 2026 will be on a {new_years_day.strftime('%A')}")

# calculate the difference between today and New year's Day:
delta = new_years_day - this_date
print(f"Number of days until New Year's Day 2026: {delta.days}")

