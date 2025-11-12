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


# Visualisation 1: ax[0,0] - Pie Chart of Survival
# set the title for the visualisation

# display the pie chart using the survival_dict dictionary


# Visualisation 2: ax[0,1] - Bar Chart of Passenger Class numbers
# set the title for the visualisation

# display horizontal gridlines

# display the bar chart using the pclass_dict dictionary


# Visualisation 3: ax[1,0] - Histogram of ages
# set the title for the visualisation

# set the label for the x-axis

# set the label for the y-axis

# display horizontal gridlines

# set the bins (intervals)

# set the x_ticks

# display the histogram using the ages_list


# Visualisation 4: ax[1,1] - scatter plot of fare vs age
# set the title for the visualisation

# set the label for the x-axis

# set the label for the y-axis

# display both horizontal and vertical gridlines

# display the scatter plot using and ages_list

# show the visualisations

# save the figure




