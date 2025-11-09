# Program Name: multiple_boxplot.py
# Purpose: To plot the fires per month in Brail
# Example of: matplotlib multiple boxplots
import matplotlib.pyplot as plt

# create an empty dictionary for the data
data_by_state = {}

# read the data from the file
with open("../examples (older)/amazon2.csv") as datafile:
    # for each line in the file
    for line in datafile:
        # split the line into the components
        year, state, month, fires, date = line.strip().split(",")

        # if this is the first occurence of this state
        if not state in data_by_state:
            # create a list with the number of fires as the first element
            data_by_state[state] = [int(fires)]
        # otherwise append to the existing list
        else:
            data_by_state[state].append(int(fires))

# create a figure and an axis object
fig, ax = plt.subplots()

# set the labels on the axes
ax.set_xlabel("Number of Fires per month")
ax.set_ylabel("State")
# set the title
ax.set_title("Fires in Brazil 1998-2017")

# do a box plot
ax.boxplot(data_by_state.values(), 
           showfliers=False, # leave out the outliers
           vert=False, # default is to draw the boxplot vertically
           labels=data_by_state.keys()) # pass in the list of labels - states
plt.show() # display

# save the image
fig.savefig('box plots/multiple_boxplots.png', bbox_inches='tight')
