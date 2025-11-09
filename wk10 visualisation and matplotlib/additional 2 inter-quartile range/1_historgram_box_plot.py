# Program to visualise Troller Watch data with a histogram, box plot and viol
# Example of: Visualisation with matplotlib
# (For simplicity, ignoring errors, i.e. no Exception Handling)

import matplotlib.pyplot as plt

# from statistics_function_1 import calc_median
import sys
sys.path.insert(1, '../examples (older)') # access calc_functons in examples (older) dir
from calc_functions import calc_median

# create a list for the patients numbers
patients_list = []

# read the data from the file
with open("trolleywatch.csv") as data_file:
    # read the first line containing the headings and discard it
    data_file.readline()

    # for each other line in the file
    for line in data_file:
        # split the line into the components
        date_string, hospital, region, trolley, ward, patients = line.strip().split(",")

        # add to the list
        patients_list.append(int(patients))

# create a fig and axes
fig, ax = plt.subplots()

# display a title
ax.set_title("Trolleywatch Box Plot")
# set a label for the y-axis
ax.set_ylabel("Number of Patients")
# Display the boxplot
ax.boxplot(patients_list)

# Calculate the interquartile range
patients_list.sort() # sort the values in order

# calculate the mid index
mid_index = int(len(patients_list)/2)

# check for an odd number of elements
if len(patients_list) % 2 == 1: # odd
    lower_half = patients_list[:mid_index] # up to but not including the mid index
    upper_half = patients_list[mid_index+1:] # from the value after the mid index to the end
else: # even
    lower_half = patients_list[:mid_index]
    upper_half = patients_list[mid_index:]

# calculate the quartiles
q1 = calc_median(lower_half) # lower quartile
# median = calc_median(patients_list)
q2 = calc_median(patients_list) # median
q3 = calc_median(upper_half) # upper quartile
iqr = q3 - q1
print(f"{q1=}")
print(f"{q2=}") # median
print(f"{q3=}")
print(f"{iqr=}")

plt.show()

fig.savefig('iqr.png', bbox_inches='tight')