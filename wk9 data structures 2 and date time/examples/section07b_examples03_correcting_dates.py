#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Program to pre-process the forest fires data, renaming the months into English

@author: cormac
"""
import datetime
import calendar

# create a dictionary which stores as items each month name and the corresponding month number
months_dict = dict(zip(calendar.month_name[1:], range(1, 13)))

# open the files
with open("amazon_english_by_date.csv", "r") as infile, open("amazon_english_correct_dates.csv", "w") as outfile:
    # read the headers from the first line of the infile and write them directly to the outfile
    outfile.write(infile.readline())
    
    # read in each line of the input file
    for line in infile:
        # split the line into component variables
        year, state, month, fires, date_string = line.strip().split(",")        
        
        # use the date string to generate a date object
        fire_date = datetime.date.fromisoformat(date_string)
        
        # use the month name to generate the correct month number
        # and inserts the correct month number in the date object
        if month != "January": # January already has the correct month number
            new_date = fire_date.replace(month=months_dict.get(month))
            # generate a date string in YYYY-MM-DD format            
            new_date_string = new_date.isoformat()
            
            # update the line with the new date
            line = line.replace(date_string, new_date_string)

        # store the line in the output file
        outfile.write(line)           
