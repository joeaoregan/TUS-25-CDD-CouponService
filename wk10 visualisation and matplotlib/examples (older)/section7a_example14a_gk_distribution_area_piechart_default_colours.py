# program to display a pie chart of the distribution areas for an international GK
# Uses the default colours for the pie chart segments

import matplotlib.pyplot as plt

# hard-coded values for the distribution areas
areas = {"Defending 3rd":2, 'Middle 3rd': 21, "Attacking 3rd": 4}

# create the figure and axes
fig,ax = plt.subplots()

# set a title which includes the total of the values from the dictionary
ax.set_title("GK Distribution Areas (Total: " + str(sum(areas.values())) + ")")

# display the pie chart using the default colours
ax.pie(areas.values(), labels=areas.keys(), autopct="%.0f%%")

# display the figure (not needed with Spyder)
plt.show()

