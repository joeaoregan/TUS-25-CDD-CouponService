"""
Program to visualise the Titanic data set
Example of: Multiple plots of different types

@author: cormac
"""
import matplotlib.pyplot as plt

# dictionary of ages by survival
survival_dict = {"survived": 0, "died": 0 }
ages_list = []
fares_list = []
pclass_dict = { "1": 0, "2": 0, "3": 0}

# open the file (deliberately leaving out exception handling, except where necessary)
with open("titanic2.csv") as data_file:
    data_file.readline() # discard the column headers
    
    for line in data_file:
        #split the line into 5 variables
        survived, pclass, name, gender, age, fare, embarked = line.split(",")        
        
        # try to convert the age to a decimal number (could be missing or invalid)
        try:
            age = float(age)
            ages_list.append(age)
            fares_list.append(float(fare))            
        except ValueError:
            print("Missing or invalid age for passenger", name)
                                    
        # update the survival dictionary
        if survived == "0":
            survival_dict["died"] +=1
        else:
            survival_dict["survived"] +=1
            
        # update the passenger class dictionary        
        pclass_dict[pclass] = pclass_dict.get(pclass, 0) + 1

# visualisations
# create the figure and axes
fig,axs = plt.subplots(2,2) # 2 rows, 2 cols

# Visualisation 1: ax[0,0] - Pie Chart of Survival
# set the title for the visualisation
axs[0,0].set_title("Survival Rate")
# display the pie chart using the survival_dict dictionary
axs[0,0].pie(survival_dict.values(), labels=survival_dict.keys(), autopct="%.0f%%")

# Visualisation 2: ax[0,1] - Bar Chart of Passenger Class numbers
# set the title for the visualisation
axs[0,1].set_title("Passenger Numbers by Class")
# display horizontal gridlines
axs[0,1].grid(axis="y")
# display the bar chart using the pclass_dict dictionary
axs[0,1].bar(pclass_dict.keys(), pclass_dict.values())

# Visualisation 3: ax[1,0] - Histogram of ages
# set the title for the visualisation
axs[1,0].set_title("Histogram of Ages")
# set the label for the x-axis
axs[1,0].set_xlabel("Age in years")
# set the label for the y-axis
axs[1,0].set_ylabel("Frequency (Number of Passengers") # as it is in the exercises pdf
# display horizontal gridlines
axs[1,0].grid(axis="y")
# set the bins (intervals)
bins = range(0, int(max(ages_list))+10, 10)
# set the x_ticks
axs[1,0].set_xticks(bins)
# display the histogram using the ages_list
axs[1,0].hist(ages_list, bins, edgecolor="black")

# Visualisation 4: ax[1,1] - scatter plot of fare vs age
# set the title for the visualisation
axs[1,1].set_title("Scatter Plot of fare vs Age")
# set the label for the x-axis
axs[1,1].set_xlabel("Age in years")
# set the label for the y-axis
axs[1,1].set_ylabel("Fare (in Pounds)")
# display both horizontal and vertical gridlines
axs[1,1].grid(axis="both")
# display the scatter plot using and ages_list
axs[1,1].scatter(x=ages_list, y=fares_list, marker=".", s=2)
# show the visualisations
plt.show()
# save the figure
fig.savefig("a00258304_titanic3.png", bbox_inches='tight')



