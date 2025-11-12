"""
Program to visualise the Titanic data set
Example of: Stacked Bar Charts

@author: cormac
"""
import matplotlib.pyplot as plt

# dictionary of survival by passenger class
survival_by_pclass = { '1':[0,0], '2':[0,0], '3':[0,0] } # index 0: number who died, index 1: number who survived

# dictionary of survival by gender
survival_by_gender = { 'female':[0,0], 'male':[0,0] } # index 0: number who died, index 1: number who survived

# open the file (deliberately leaving out exception handling, except where necessary)
with open("titanic2.csv") as data_file:
    data_file.readline() # discard the column headers
    
    for line in data_file:
        #split the line into 5 variables
        survived, pclass, name, gender, age, fare, embarked = line.strip().split(",")        
        # convert survived from string to int
        survived = int(survived)
        # update the dictionary
        survival_by_pclass[pclass][survived] = survival_by_pclass[pclass][survived] + 1
        survival_by_gender[gender][survived] = survival_by_gender[gender][survived] + 1
        
    # use a list comprehension to get the numbers who died by passenger class 
    # index 0 gives the first number (died) of each values list
    died_by_class_list = [ value[0] for value in survival_by_pclass.values() ] 
    # use a list comprehension to get the numbers who survived by passenger class 
    # index 1 gives the second number (survived) of each values list
    survived_by_class_list = [ value[1] for value in survival_by_pclass.values() ] 
    # use a list comprehension to get the numbers who died by gender
    died_by_gender_list = [ value[0] for value in survival_by_gender.values() ]
    # use a list comprehension to get the numbers who survived by gender
    survived_by_gender_list = [ value[1] for value in survival_by_gender.values() ]        


# visualisations
# create the figure and axes

# Visualisation 1: axs[0] Stacked Bar Chart of Survivors by passenger class
# set the title x-axis and y-axis for the visualisation

# display bar chart using the survival_by_pclass dictionary keys and survived_by_class_list
# display bar chart using the survival_by_pclass dictionary keys and died_by_class_list
# display a legend
    
# Visualisation 2: axs[1] - Stacked Bar Chart of Survivors by gender
# set the title, x-axis and y-axis for the visualisation

# display stacked bar chart using the survival_by_gender dictionary keys and and survived_by_gender_list
# display stacked bar chart using the survival_by_gender dictionary keys and and died_by_gender_list
# display a legend

# show the visualisation

# save the figure
