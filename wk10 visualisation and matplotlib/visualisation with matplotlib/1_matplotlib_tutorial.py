# Visualisation with Matplotlib

# Matplotlib is a Python 2D plotting library which producdes publication quality figures in a variety of formats and interactive environments.
# https://matplotlib.org/3.1.1/index.html


# Create visualisations such as: Line plots, bar charts, pie charts, scatter plots, date plots, box plots


# Importing Matplotlib
# importing is usually done as follows:
# import matplotlib.pyplot as plt

# Matbplotlib is a third-party library, which means it must be installed before you can use it. It's installed automatically with Anaconda.

# If you're not using Anaconda, you'll need to install it,
# e.g. using pip: pip install matplotlib


# Object-Oriented Interface

# Object | Purpose
# Figure | Container for one or more Axes instances
# Axes   | Rectangular areas to hold the basic elements, such as lines, text, and so on

# Figure is the image that may contain 1 or more Axes.

# Axes represent indiviual plots
# https://matplotlib.org/3.1.1/tutorials/introductory/lifecycle.html


# Creating the Visualisations

# Create an instance of Figure and an instance of Axes:
# fig, ax = plt.subplots()

# The Figure is like a canvas, and the Axes is a part of that canvas on which we will make a particular visualization.

# Figures can have multiple axes on them (multiple visualisations).


# Visualisation Methods

# Method         | Description
# -------------- | ---------------------------------------------------------------------------
# ax.plot()      | Create a line plot (line graph)
# ax.boxplot()   | Create a box plot, which identifies the median (middle value) and quartiles
# ax.plot_date() | Create a date plot, which displays the values over time
# ax.bar()       | Create a (vertical) bar chart
# ax.barh()      | Create a horizontal bar chart
# ax.pie()       | Create e pie chart
# ax.acatter()   | Create a scatter plot, which displays the values as (x, y) pairs


# Additional Methods

# Method               | Description
# -------------------- | ---------------------------------------------------------------------------
# ax.set_title()       | Set a title for the visualisation
# ax.set_xlabel()      | Set a label on the x-axis
# ax.set_ylabel()      | Set a label on the y-axis
# ax.set_xticks()      | Set the "tick" markers on the x-axis
# ax.set_yticks()      | Set the "tick" markers on the y-axis
# ax.set_xticklabels() | Set the labels for the "tick" markers on the x-axis
# ax.set_yticklabels() | Set the labels for the "tick" markers on the y-axis

# Display the visualisation(s) use: plt.show()
# Save the figure, use: fig.savefig(filename)

