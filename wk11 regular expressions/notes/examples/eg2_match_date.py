# More Complex Regular Expressions

# Many logfiles represent dates in the form YYYY-MM-DD
# An initial attempt to define a regular expression to match a date in this format is:
# [0-9]{4}-[0-9]{2}-[0-9]{2}
# This will correctly match valid dates, e.g.:    2020-03-05
# but will incorrectly match invalid dates, e.g.: 2020-99-99
# This regex can't be used for date validation, but could be used for date searches.

import re

def check_date(date):
    # compare the regex to the string
    match = re.fullmatch("[0-9]{4}-[0-9]{2}-[0-9]{2}", date)

    # check if there's a match
    if match:
        print("Valid date")
    else:
        print("Invalid date")


check_date("2020-03-05") # Valid date
check_date("2020-99-99") # Valid date - ???
