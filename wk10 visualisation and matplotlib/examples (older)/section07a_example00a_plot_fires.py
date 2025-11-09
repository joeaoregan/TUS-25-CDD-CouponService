# Program Name: section06_example00a_plot_fires.py
# Purpose: To plot the fires per month in Acre state, 2016
# Example of: Matplotlib plot with data in lists
import matplotlib.pyplot as plt

# Set the data
fires = [12, 5, 0, 0, 21, 87, 533, 2188, 3586, 509, 46, 6]
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", 
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

# Create the figure and axes
fig, ax = plt.subplots()

# Set the title
ax.set_title("Fires per Month in Acre, 2016")

# set the axis labels
ax.set_xlabel("Months")
ax.set_ylabel("Number of Fires")

# plot the values
ax.plot(months, fires)

# show the plot
plt.show()

# Save the figure (bbox = "tight" eliminates whitespace padding)
fig.savefig("acre_fires_2016.png", bbox_inches="tight")
