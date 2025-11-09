# Programm Name: add_subplot.py
# Purpose: Plot Amazon Fires by State
# Example of: Multiple Subplots on a Figures - alternative syntax using add_subplot
import datetime

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

print("This program processes forest fire data")

# start with an empty dictionary
# dictionary keys will be the (state, year, month)
# corresponding values will be the (date, number of fires)
data = {}

# date format string
format_str = "%Y-%m-%d"

print()
print("Fires per month in Brazil, 1998-2017")
# open the file
with open("../examples (older)/amazon2.csv") as data_file:
    # read in the first line containing the headers
    headers = data_file.readline()

    # for each other line in the file
    for line in data_file:
        # split each line into components (remove white space from ends of line)
        year, state, month, fires, date = line.strip().split(",")

        # insert hte data into the dictionary (converting dates into datetime objects)
        data[(state, int(year), month)] = (datetime.datetime.strptime(date, format_str),int(fires))

print()
print(f"Number of values: {len(data)}")

# create a list of states
states = []

# go through each key in the dictionary
for state,year,month in data.keys():
    # if we haven't already seen this state
    if state not in states:
        # add it to the list of states
        states.append(state)


# create a figure
fig = plt.figure() # figure is a canvas to store all the plots

# create a new empty dictionary
# the dictionary keys are the state names
# the values are the list of fires in that state
data_by_state = {}
i = 1 # index for the subplots

# format the ticks
months = mdates.MonthLocator() # every month

# set the title
fig.suptitle("Fires in Brazil 1998-2017")

# for each state in the list of states
for state in states:
    # insert the state along with the (list of dates and list of fires) for that state
    data_by_state[state] = [ value[0] for key,value in data.items() if key[0] == state ],[value[1] for key,value in data.items() if key[0] == state ]

    # date plot for each state
    ax = fig.add_subplot(6,4,i) # 6 rows, 4 columns (only 23 states, 1 will be blank)
    ax.plot_date(mpl.dates.date2num(data_by_state[state][0]),data_by_state[state][1], marker=",", linestyle="-")

    i += 1

# shot the plots
plt.show()

fig.savefig('multiple/amazon_date_plots.png', bbox_inches='tight')