#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Program to determine the earliest and latest dates in the Forest Fires csv file
Example of: working with datetime.date

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
# date objects can be compared using max() and min() functions
print(f"Earlist date: {min(dates_list).strftime('%d/%m/%Y')}") 
print(f"Latest date: {max(dates_list).strftime('%d/%m/%Y')}")

