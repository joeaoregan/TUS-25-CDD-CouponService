# A00258304

# The time (in seconds) to download a file based on the size of the file (in MB) and the speed of the connection (in Mbps) 
# is given by the formula:
# time = (filesize x 8.388608) / connection speed

# Write a Python program which inputs the size of a file and the download speed and 
# then calculates and displays the download time for the file, correct to 2 decimal places.

# Example:

# Input  | Result
# -------|-------------------------------------------
# 10     | Enter the file size in MB: 10
# 1.544  | Enter the connection speed in Mbps: 1.544
#        | Download time is 54.33 seconds
# -------|-------------------------------------------
# 210    | Enter the file size in MB: 210
# 44.736 | Enter the connection speed in Mbps: 44.736
#        | Download time is 39.38 seconds
# -------|-------------------------------------------
# 4.5    | Enter the file size in MB: 4.5
# 5      | Enter the connection speed in Mbps: 5
#        | Download time is 7.55 seconds

filesize_mb = float(input("Enter the file size in MB: "))
connection_speed_mbps = float(input("Enter the connection speed in Mbps: "))

download_time = (filesize_mb * 8.388608) / connection_speed_mbps

print(f"Download time is {download_time:.2f} seconds")