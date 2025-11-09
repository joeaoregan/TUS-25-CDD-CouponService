# Program Name: section06_example02_bar_chart_with_values.py
# Purpose: To display a bar chart of the fires per state in Brazil
# Example of: matplotlib horizontal bar chart
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

# create a figure and an axis object
fig, ax = plt.subplots()

# set the title
ax.set_title("Fires in Acre State, Brazil 1998-2017")

# set the x positions
y_pos = [ i for i in range(len(data_by_state))]

# set the y tick labels
ax.set_yticks(y_pos)
ax.set_yticklabels(data_by_state.keys())

# set the labels on the axes
ax.set_ylabel("State")
ax.set_xlabel("Total Number of Fires")

# display the value at the end of each bar
# enumerate returns each value and its index in a tuple (index,value)
for index, value in enumerate(data_by_state.values()):
    # the text function displays text at a specific location
    # the syntax is text(x, y, text_string)
    ax.text(value, index-0.25, str(value))

# draw the horizontal bar chart
ax.barh(y_pos,data_by_state.values(), align="center")
plt.show()

# save the bar chart
fig.savefig('amazon_hbar_chart.png', bbox_inches='tight')

