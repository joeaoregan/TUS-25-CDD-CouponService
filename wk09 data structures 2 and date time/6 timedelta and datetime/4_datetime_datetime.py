# datetime.datetime
# A datetime object is a combination of a date and a time

# The class method now() returns the local date and time:

import datetime

print(datetime.datetime.now()) # 2025-11-08 21:11:36.117467

print(datetime.datetime.now(datetime.UTC)) # 2025-11-08 21:11:36.117568+00:00