# Program Name: section06_example09_dateplots.py
# Purpose: Plot Amazon Fires by State
# Example of: Multiple Plots on a single Axes
import datetime

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
with open("amazon2.csv") as data_file:
    # read in the first line containing the headers
    headers = data_file.readline()
    
    # for each other line in the file
    for line in data_file:
        # split each line into components (remove white space from ends of line)
        year, state, month, fires, date = line.strip().split(",")

        # insert the data into the dictionary (converting dates into datetime objects)
        data[(state, int(year), month)] = (datetime.date.fromisoformat(date),int(fires))

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

# create a figure and an axis object
fig, ax = plt.subplots()

# format the ticks
months = mdates.MonthLocator()  # every month
ax.xaxis.set_minor_locator(months)

# set the labels on the axes
ax.set_xlabel("Time")
ax.set_ylabel("Number of Fires per month")

# set the title
ax.set_title("Fires in Acre State, Brazil 1998-2017")

      
# data by state
print()        
print(f"{'State':16}  Total")        
# create a new empty dictionary
# the dictionary keys are the state names
# the values are the list of fires in that state
data_by_state = {} 
# for each state in the list of states
for state in [ "Acre", "Para" ]:
    # insert the state along with the (list of dates and list of fires) for that state
    data_by_state[state] = [ value[0] for key,value in data.items() if key[0] == state ],[ value[1] for key,value in data.items() if key[0] == state ]
    
    # date plot for the current state
    ax.plot_date(data_by_state[state][0], data_by_state[state][1], marker = ",", linestyle="-")

# manually set a legend
ax.legend([ "Acre", "Para" ])
plt.show()

fig.savefig('amazon_date_plot.png', bbox_inches='tight')

    
    
    
