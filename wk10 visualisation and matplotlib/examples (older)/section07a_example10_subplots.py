# Program Name: section06_example10_subplots.py
# Purpose: To plot the fires per month in Brazil
# Example of: matplotlib multiple subplots: bar chart and pie chart
import matplotlib.pyplot as plt

# create an empty dictionary
data_by_state = {}

# read the data from the file
with open("amazon2.csv") as datafile:
    #for each line in the file
	for line in datafile:
        # split the line into the components
	    year, state, month, fires, date = line.strip().split(",")
		
	    # if this is the first occurence of this state
	    if not state in data_by_state:
		    data_by_state[state] = int(fires) 
	    # otherwise add to the existing value
	    else:
		    data_by_state[state] += int(fires)

# create a figure and an axis object using a subplot grid: 2 rows, 1 column
fig, ax = plt.subplots(2)

# set the title
fig.suptitle("Fires in Acre State, Brazil 1998-2017")

# set the x positions
y_pos = [ i for i in range(len(data_by_state))]

# set the y tick labels
ax[0].set_yticks(y_pos)
ax[0].set_yticklabels(data_by_state.keys())

# set the labels on the axes
ax[0].set_ylabel("State")
ax[0].set_xlabel("Total Number of Fires")

# do a horizontal bar chart on the first row
ax[0].barh(y_pos,data_by_state.values(), align="center")
# do a pie chart on the second row
ax[1].pie(data_by_state.values(), labels = data_by_state.keys())

plt.show()

# save the bar chart
fig.savefig('amazon_hbar_pie.png', bbox_inches='tight')

