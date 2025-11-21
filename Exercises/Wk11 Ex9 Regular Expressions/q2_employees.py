# A00258304

import re

employees_dict = {}

with open('employees.txt') as data_file:
    for line in data_file:
        result = re.search(r"(\d{7}[a-zA-Z]{2}) (\d+)", line)
        if result:
            # print(result.group(1), result.group(2)) # ppsn, salary
            employees_dict[result.group(1)] = int(result.group(2))


print("PPSN of employee with the highest salary:", max(employees_dict,key=employees_dict.get))