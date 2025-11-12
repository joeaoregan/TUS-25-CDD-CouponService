"""
Program to visualise the Titanic data set
Example of: Multiple Pie Charts

@author: cormac
"""
import matplotlib.pyplot as plt

# dictionary of ages by survival
survival_by_gender = {}
survival_by_pclass = {}
survival_by_port = {}

# open the file (deliberately leaving out exception handling, except where necessary)
with open("titanic2.csv") as data_file:
    data_file.readline() # discard the column headers
    
    for line in data_file:
        #split the line into 5 variables
        survived, pclass, name, gender, age, fare, embarked = line.strip().split(",")        
        
        # update the dictionary
        if survived == "1":
            survival_by_gender[gender] = survival_by_gender.get(gender,0) + 1
            survival_by_pclass[pclass] = survival_by_pclass.get(pclass,0) + 1
            if embarked:
                survival_by_port[embarked] = survival_by_port.get(embarked,0) + 1         

# visualisations
# create the figure and axes

# Visualisation 1: ax[0] - Pie Chart of Survivors by Gender
# set the title for the visualisation

# display pie chart using the survival_by_gender dictionary


# Visualisation 2: ax[1] - Pie Chart of Survivors by Pclass
# set the title for the visualisation

# display pie chart using the survival_by_pclass dictionary


# Visualisation 3: ax[2] - Pie Chart of Survivors by Port of Embarcation
# set the title for the visualisation

# display pie chart using the survival_by_port dictionary


# show the visualisation

# save the figure

