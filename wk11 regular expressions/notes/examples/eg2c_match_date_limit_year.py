#  The regex for the year [0-9]{4} means any number from 0000 to 9999.
# If you wanted to limit it to a value between 1900-2099, you could use the following:
#  (19|20)[0-9]{2}
# which means 19 or 20 followed by 2 digits.
import re

def check_date_limit_year(date):
    match = re.fullmatch("(19|20)[0-9]{2}-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])", date)

    if match:
        print("Valid date")
    else:
        print("Invalid date")
        

check_date_limit_year("2020-03-05") # Valid date
check_date_limit_year("3030-99-99") # Invalid date

