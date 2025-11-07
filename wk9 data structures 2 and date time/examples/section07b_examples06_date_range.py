#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Program to determine the range of dates in the Forest Fires csv file
Example of: working with datetime.date and datetime.timedelta

@author: cormac
"""
import datetime

dates_list = []

# open the files
with open("amazon_english_correct_dates.csv", "r", encoding="utf-8") as infile:
    # read the headers from the first line of the infile and discard
    infile.readline()
    
    # read in each line of the input file
    for line in infile:
        # split into components, ignoring all but the date_string
        _, _, _, _, date_string = line.strip().split(",")

        # convert the date string to a date object and add it to the list
        dates_list.append(datetime.date.fromisoformat(date_string))
        
# Results
print(f"Number of dates: {len(dates_list)}")
# the date objects can be compared using max() the min()
earliest = min(dates_list)
print(f"Earlist date: {earliest}")
latest = max(dates_list)
print(f"Latest date: {latest}")

# determine the range of dates, the difference between the latest and earliest
delta = latest - earliest
print(f"Number of days between the earliest and latest dates: {delta.days}")

