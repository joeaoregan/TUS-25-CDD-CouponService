#  Non-Capturing: (?:)
# An IPv4 address includes 3 dots, separating the four octets: 192.168.26.10.  
# simple regex for an IPv4 address is:  ^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$
# or alternatively:                     ^(\d{1,3}\.){3}\d{1,3}$

import re

def valid_ip_regex(regex):
    ipv4 = "192.168.26.10"
    match = re.fullmatch(regex, ipv4) # simple regex

    if match:
        print("Valid IPv4")
    else:
        print("Not a valid IPv4")


simple_regex =      r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$"
alternate_regex =   r"^(\d{1,3}\.){3}\d{1,3}$"
capture_regex =     r"(\d{1,3}\.){3}\d{1,3}"

valid_ip_regex(simple_regex)
valid_ip_regex(alternate_regex)
valid_ip_regex(capture_regex)