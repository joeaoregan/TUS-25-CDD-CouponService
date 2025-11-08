#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Program to calculate the date with the most transferss
"""
# Example: FTP File Transfer Log xferlog

# Determine date with most file transfers using a dictionary
#    (key=date object, value=number of transfers on that date)
# 1. Reads in the contents of the file one line at a time
# 2. Extracts date and time infomration from first 24 characters of each line
# 3. Creates a date object
# 4. Updates dictionary (adds 1 to transfer count)

import datetime
transfers = {} # number of transfers per day

# open the file
with open("../examples/xferlog") as logfile:
    # read in the lines one at a time
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


# Output:
# Date of first file transfer: 2019-03-08
# Date of last file transfer: 2019-03-23
# Date with most transfers: 2019-03-12


print(transfers)
print(transfers.keys())
print(list(transfers.keys()))
print(list(transfers.keys())[0]) # first date
print(list(transfers.keys())[0].strftime("%d/%m/%y")) # 08/03/19
print(list(transfers.keys())[0].strftime("%d/%m/%Y")) # 08/03/2019
print(list(transfers.keys())[-1].strftime("%d/%m/%Y")) # 23/03/2019 -- last date object in the keys

