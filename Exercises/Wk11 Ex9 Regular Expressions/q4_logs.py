# A00258304

import re

filename = input("Enter the filename: ")

status_codes_dict = {}

regex = re.compile(r"(HTTP/1.[01])\" (\d{3})")

with open(filename) as logfile:
    for line in logfile:
        match = regex.search(line)

        if match:
            # print(match.group(1), match.group(2))
            status_codes_dict[match.group(2)] = status_codes_dict.get(match.group(2), 0) + 1
            

# print(status_codes_dict)
print("Code Frequency")
for code in sorted(status_codes_dict):
    print(f"{str(code):6} {status_codes_dict[code]:>6}")

