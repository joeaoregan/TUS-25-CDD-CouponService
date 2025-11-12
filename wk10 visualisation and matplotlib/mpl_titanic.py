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
with open("examples/titanic2.csv") as data_file:
    data_file.readline() # discard the column headers
    
    for line in data_file:
        #split the line into 5 variables
        survived, pclass, _, gender, _, _, _ = line.strip().split(",")        
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
fig, axs = plt.subplots(1,2) # 1 row, 2 cols
# Visualisation 1: axs[0] Stacked Bar Chart of Survivors by passenger class
# set the title x-axis and y-axis for the visualisation
axs[0].set_title("Survival by Class")
axs[0].set_xlabel("Passenger Class")
axs[0].set_ylabel("Number of Passengers")

# display bar chart using the survival_by_pclass dictionary keys and survived_by_class_list
axs[0].bar(survival_by_pclass.keys(), survived_by_class_list)
# display bar chart using the survival_by_pclass dictionary keys and died_by_class_list
axs[0].bar(survival_by_pclass.keys(), died_by_class_list, bottom=survived_by_class_list)
# display a legend
axs[0].legend(['Survived','Died'])
# Visualisation 2: axs[1] - Stacked Bar Chart of Survivors by gender
# set the title, x-axis and y-axis for the visualisation
# axs[1].set_title("Survival by Gender")
# axs[1].set_xlabel("Passenger Gender")
# axs[1].set_ylabel("Number of Passengers")
axs[1].set(title="Survival by Gender", xlabel="Passenger Gender", ylabel="Number of Passengers")
# display stacked bar chart using the survival_by_gender dictionary keys and and survived_by_gender_list
axs[1].bar(survival_by_gender.keys(), survived_by_gender_list, label="Survived")
# display stacked bar chart using the survival_by_gender dictionary keys and and died_by_gender_list
axs[1].bar(survival_by_gender.keys(), died_by_gender_list, bottom=survived_by_gender_list, label="Died")
# display a legend
axs[1].legend(loc="upper right")
# show the visualisation
plt.show()
# save the figure
fig.savefig("titanic.png")