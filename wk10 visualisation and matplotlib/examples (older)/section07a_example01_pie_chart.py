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
		    data_by_state[state] = int(fires)
	    # otherwise add to the existing value
	    else:
		    data_by_state[state] += int(fires)
	
# create a figure and an axis object
fig, ax = plt.subplots()

# set the title
ax.set_title("Fires in Acre State, Brazil 1998-2017")

# do a pie chart
ax.pie(data_by_state.values(), labels = data_by_state.keys(),autopct="%.0f%%")
plt.show()

# save the file
fig.savefig('amazon_pie_chart.png', bbox_inches='tight')

