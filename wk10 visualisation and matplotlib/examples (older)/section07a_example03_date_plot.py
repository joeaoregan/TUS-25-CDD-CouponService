# Program Name: section06_example03_date_plot.py
# Purpose: To plot the fires per month in Acre, Brazil
# Example of: matplotlib date plot

import datetime

import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# create a empty lists for the data
x_dates = []
y_fires = []

# date format string
format_str = "%Y-%m-%d"

# read the data from the file
with open("amazon2_Acre.csv") as datafile:
	# for each line in the file
	for line in datafile:
		# split the line into the components
		year, state, month, fires, date = line.strip().split(",")
		
		# insert into lists
		# convert date in string format to a datetime object
		x_dates.append(datetime.date.fromisoformat(date))
		y_fires.append(int(fires))
		

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

# draw the date plot
ax.plot_date(x_dates, y_fires, marker = ",", linestyle="-")
plt.show()

# save the image
fig.savefig('acre_date_plot.png', bbox_inches='tight')

