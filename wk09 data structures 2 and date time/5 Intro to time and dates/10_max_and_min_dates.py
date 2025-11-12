# max() and min()

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

        # convert the dates string to a date object and add it to the list
        dates_list.append(datetime.date.fromisoformat(date_string))

# Results
print(f"Number of dates: {len(dates_list)}") # Number of dates: 6454
# date objects can be compared using max() and min() functions
# print(f"Earliest date: {min(dates_list)}") # Earliest date: 1998-01-01
# print(f"Latest date: {max(dates_list)}") # Latest date: 2017-11-01

# return a string with day, month, year dd/mm/yyyy instead of ISO format
print(f"Earliest date: {min(dates_list).strftime('%d/%m/%Y')}") # Earliest date: 01/01/1998
print(f"Latest date: {max(dates_list).strftime('%d/%m/%Y')}") # Latest date: 01/11/2017