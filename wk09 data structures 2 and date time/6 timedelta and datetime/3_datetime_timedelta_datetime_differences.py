import datetime

dates_list = []

# open the files
with open("../examples/amazon_english_correct_dates.csv", "r", encoding="utf-8") as infile:
    # read the headers from the first line of the infile and discard
    infile.readline()

    # read in each line of the input file
    for line in infile:
        # split into components, ignoring all but the date_string
        _, _, _, _, date_string = line.strip().split(",")

        # convert the date string to a date object and add it to the list
        dates_list.append(datetime.date.fromisoformat(date_string))

# Results
print(f"Number of dates: {len(dates_list)}") # Number of dates: 6454
# the date objects can be compared using max() and min()
earliest = min(dates_list)
print(f"Earliest date: {earliest}") # Earliest date: 1998-01-01
latest = max(dates_list)
print(f"Latest date: {latest}") # Latest date: 2017-11-01

# determine the range of dates, the difference between the latest and earliest
delta = latest - earliest
print(f"Number of days between the earliest and latest dates: {delta.days}") # Number of days between the earliest and latest dates: 7244

# Output:
# Number of dates: 6454
# Earliest date: 1998-01-01
# Latest date: 2017-11-01
# Number of days between the earliest and latest dates: 724