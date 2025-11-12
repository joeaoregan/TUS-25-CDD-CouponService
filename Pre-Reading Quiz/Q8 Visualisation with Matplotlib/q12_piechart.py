import matplotlib.pyplot as plt

data = {"derp": 10, "derp2": 20, "derp3": 50, "derp4": 5}


# create a figure and an axis object
fig, ax = plt.subplots()

# set the title
ax.set_title("Question 12")

# do a pie chart
# ax.pie(data.values(), labels = data.keys(),autopct="%.0f%%") # Specify the percentage to the nearest integer
# ax.pie(data.values(), labels = data.keys())

# a.
# ax.pie(data.values()) # works, no labels

# b.
# ax.pie(labels=data.keys(), data.values()) # SyntaxError: positional argument follows keyword argument

# c.
ax.pie(data.values(), labels=data.keys()) # This?

# d.
# ax.pie(data.keys(), data.values()) # ValueError: could not convert string to float: 'derp'

# e.
# ax.pie(data.values(), data.keys()) # TypeError: can't multiply sequence by non-int of type 'float'

plt.show()