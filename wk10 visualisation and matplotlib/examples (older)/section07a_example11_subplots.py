# Program Name: section06_example11_subplots.py
# Purpose: Plot Amazon Fires by State
# Example of: Multiple Subplots on a Figure - using subplots(2,2)
# Sharing x-axis between plots
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
     
# data by state
print()        
# create a new empty dictionary
# the dictionary keys are the state names
# the values are the list of fires in that state
data_by_state = {} 
# for each state in the list of states
for state in [ "Acre", "Mato Grosso", "Para", "Tocantins" ]:
    # insert the state along with the (list of dates and list of fires) for that state
    data_by_state[state] = [ value[0] for key,value in data.items() if key[0] == state ],[ value[1] for key,value in data.items() if key[0] == state ]


# create a figure and an axis object
fig, ax = plt.subplots(2,2,sharex=True)

# format the ticks
months = mdates.MonthLocator()  # every month
ax[0,0].xaxis.set_minor_locator(months)

# set the title
fig.suptitle("Fires in Acre State, Brazil 1998-2017")    
    
# date plot for each state
ax[0,0].set_title("Acre")
ax[0,0].set_ylabel("Fires per month")
ax[0,0].plot_date(data_by_state["Acre"][0], data_by_state["Acre"][1], marker = ",", linestyle="-")

ax[0,1].set_title("Mato Grosso")
ax[0,1].plot_date(data_by_state["Mato Grosso"][0], data_by_state["Mato Grosso"][1], marker = ",", linestyle="-")

ax[1,0].set_title("Para")
ax[1,0].set_xlabel("Time")
ax[1,0].set_ylabel("Fires per month")
ax[1,0].plot_date(data_by_state["Para"][0], data_by_state["Para"][1], marker = ",", linestyle="-")

ax[1,1].set_title("Tocantins")
ax[1,1].set_xlabel("Time")
ax[1,1].plot_date(data_by_state["Tocantins"][0], data_by_state["Tocantins"][1], marker = ",", linestyle="-")

# show the plots
plt.show()

fig.savefig('amazon_date_plot.png', bbox_inches='tight')

    
    
    
