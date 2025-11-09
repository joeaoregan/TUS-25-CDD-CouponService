# Program Name: section06_example01_pie_chart.py
# Purpose: To plot the fires per month in Brazil
# Example of: matplotlib pie chart
import matplotlib.pyplot as plt

# create an empty dictionary
data_by_state = {}

# read the data from the file
with open("amazon2.csv") as datafile:    
    # for each line in the file
    for line in datafile:
        # split the line into the components
        year, state, month, fires, date = line.strip().split(",")
        
        # if this is the first occurence of this state
        if not state in data_by_state:
            data_by_state[state] = int(fires), 1
        # otherwise add to the existing value
        else:
            updated_total = data_by_state[state][0] + int(fires)
            updated_number = data_by_state[state][1] + 1
            data_by_state[state] = updated_total, updated_number
    
# create a figure and an axis object
fig, ax = plt.subplots()

# set the title
ax.set_title("Fires in Acre State, Brazil 1998-2017")

# calculate the average number of fires per month for each state
averages = [ value[0]/value[1] for value in data_by_state.values() ]

# do a pie chart
ax.pie(averages, labels = data_by_state.keys(),autopct="%.0f%%")
plt.show()

# save the file
fig.savefig('amazon_pie_chart.png', bbox_inches='tight')

