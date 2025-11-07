#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Program to calculate the date with the most transfers
Example of: datetime module
@author: cormac
"""
import datetime

transfers = {} # number of transfers per day

# open the file
with open("xferlog") as logfile:
    #  read in the lines one at a time
    for line in logfile:
        # extract the date and time information from the first 24 characters of each line
        datetime_string = line[:24]
        # create a date object from the transfer timestamp
        transfer_date = datetime.datetime.strptime(datetime_string, "%a %b %d %H:%M:%S %Y").date()
        
        # Update the count for this date
        transfers[transfer_date] = transfers.get(transfer_date,0) + 1

print(f"Date of first file transfer: {min(transfers)}")
print(f"Date of last file transfer: {max(transfers)}")
print(f"Date with most transfers: {max(transfers,key=transfers.get)}")

