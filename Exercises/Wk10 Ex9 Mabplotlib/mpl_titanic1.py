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
fig,ax = plt.subplots()
# fig.suptitle("Joe O'Regan - A00258304")
# set the title for the visualisation
ax.set_title("Age Comparison of Survivors vs Non-Survivors")
# set the label for the y-axis
ax.set_ylabel("Age in years")
# display horizontal gridlines
ax.grid(axis="y")
# display multiple box plots using the dictionary
ax.boxplot(ages_by_survival.values(), 
           tick_labels=ages_by_survival.keys(),
           showmeans=True,
           meanline=True)
# show the visualisation
plt.show()
# save the figure
fig.savefig("a00258304_titanic1.png", bbox_inches='tight')