# Program Name: plot_fires.py
# Purpose: To plot the fires per month in Acre state, 2016
# Example of: Matplotlib plot
import matplotlib.pyplot as plt

# Set the data
fires = [12, 5, 0, 0, 21, 87, 533, 2188, 3586, 509, 46, 6]

# Create the figure and axes
fig, ax = plt.subplots()

# Set the title
ax.set_title("Fires per Month in Acre, 2016")

# set the axis labels
ax.set_xlabel("Time")
ax.set_ylabel("Number of Fires")

# plot the values
ax.plot(fires) # plots the 12 values in the fires list above, creating a line graph

# show the plot
plt.show()

# Save the figure (bbox = "tight" eliminates whitespacing padding)
fig.savefig("plots/acre_fires_2016.png", bbox_inches="tight")