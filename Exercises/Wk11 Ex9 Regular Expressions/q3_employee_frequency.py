# A00258304

import re

employees_freq = {}

with open('employees.txt') as data_file:
    # global contents 
    contents = data_file.read()

    department_list = re.findall(r"([A-Z][a-z]+)\n", contents)

    for department in department_list:
        employees_freq[department] = employees_freq.get(department,0) + 1

         
print("Department with most employees:", max(employees_freq,key=employees_freq.get))

# print(employees_freq)
# print(len(employees_freq))
# print(contents)