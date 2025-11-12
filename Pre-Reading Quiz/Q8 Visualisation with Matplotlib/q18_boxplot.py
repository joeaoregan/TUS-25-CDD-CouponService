# Question 18

# The variable data_dict contains a dictionary where the keys represent categories and the 
# corresponding values are lists of numbers representing data values in the category. 
# Which of the following is the correct code to display a boxplot of the values with the axes object ax?

import matplotlib.pyplot as plt

data_dict = {} # create an empty dictionary for the data

# read the data from the file
with open("../examples (older)/amazon2.csv") as datafile:
    # for each line in the file
    for line in datafile:        
        _, state, _, fires, _ = line.strip().split(",") # split the line into the relevant components 
        data_dict[state] = int(fires) # insert into the dictionary

fig, ax = plt.subplots() # create figure and an axis objects

ax.set(title="Question 18", ylabel="Number of Fires per month") # set the labels on the axes

ax.boxplot(data_dict.values(),showfliers=False) # show outliers with whiskers
# ax.boxplot(data_dict.values()) # leave out whiskers
plt.show() # display