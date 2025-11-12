# Example: Fixing dates in CSV file

# Problem: Incorrect month numbers

# Solution
# 1. Reads each line of the file and gets date string
# 2. Uses the date string to generate a date object
# 3. Uses the month name to generate the correct month number
# 4. Inserts the correct month number in the date object
# 5. generates a date string in YYYY-MM-DD format
# 6. Writes the corrected data line to a new file.

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

        # usee the date string to generate a date object
        fire_date = datetime.date.fromisoformat(date_string)

        # use the month name to generate the correct month number
        # and inserts the correct month number in the date object
        if month != "January": # January already has the correct month number
            new_date = fire_date.replace(month=months_dict.get(month)) # fix the month number
            # generate a date string in YYYY-MM-DD format
            new_date_string = new_date.isoformat() # turn it into ISO format

            # update the line with the new date
            line = line.replace(date_string, new_date_string) # put that into a new line that will go into the output file

        # store the line in the output file
        outfile.write(line)
