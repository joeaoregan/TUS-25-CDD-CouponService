"""
Program to visualise the Titanic data set
Example of: Multiple Box plots

@author: cormac
"""
import matplotlib.pyplot as plt

# dictionary of ages by survival
ages_by_survival = {"survived": [], "died": [] }

# open the file (deliberately leaving out exception handling, except where necessary)
with open("titanic2.csv") as data_file:
    data_file.readline() # discard the column headers
    
    for line in data_file:
        #split the line into 5 variables
        survived, pclass, name, gender, age, fare, embarked = line.split(",")        
        
        # try to convert the age to a decimal number (could be missing or invalid)
        try:
            age = float(age)
                        
            # update the dictionary
            if survived == "0":
                ages_by_survival["died"].append(age)
            else:
                ages_by_survival["survived"].append(age)
        except ValueError:
            print("Missing or invalid age for passenger", name)
            

# visualisations
# create the figure and axes

# set the title for the visualisation

# set the label for the y-axis

# display horizontal gridlines

# display multiple box plots using the dictionary

# show the visualisation

# save the figure
