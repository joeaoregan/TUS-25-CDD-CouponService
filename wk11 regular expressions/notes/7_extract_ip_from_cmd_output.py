# Program 7: Extract an IP address from command output

# The following program uses re.search() to find the first IP address 
# in the output from "ip a" (on Windows use ipconfig)


# Regular expressions in Python
# Example of capturing output from a command
import re
from subprocess import getoutput

# run the ip a command and store the output
# output = getoutput("ip a") # Linux
output = getoutput("ipconfig") # windows

# search for the first IP address
match = re.search(r"(?:\d{1,3}\.){3}\d{1,3}", output)

if match:
    # print the IPv4 addresses found
    print("First IP address found:", match.group())
else:
    print("No IPv4 address found")

print(match.group(0))