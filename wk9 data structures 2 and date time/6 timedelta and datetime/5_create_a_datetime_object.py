# datetime.datetime
# Create a datetime object
# datetime(year, month, day, hour, minute, seconds, microseconds)

import datetime
berlin_wall = datetime.datetime(1989,11,8,17,53)
print(berlin_wall.strftime("%I.%M %p %A %d %B %Y")) # 05.53 PM Wednesday 08 November 1989


# class method formisoformat(datetime_string) returns a datetime object
# using a string in ISO format YYYY-MM-DD HH:MM:SS

vostok_launch = datetime.datetime.fromisoformat("1961-04-12 06:07")
print(vostok_launch) # 1961-04-12 06:07:00
print(vostok_launch.strftime("%I.%M %p %A %d %B %Y")) # 06.07 AM Wednesday 12 April 1961