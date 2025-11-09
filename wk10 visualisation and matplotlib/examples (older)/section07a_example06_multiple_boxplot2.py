# Program Name: section06_example06_multiple_boxplot2.py
# Purpose: Display boxplots for triple jump results
# Example of: Matplotlib multiple boxplots
import matplotlib.pyplot as plt

print("This program displays multiple box plots")

# create an empty dictionary to store the results
# dictionary key is the name of the competitor
# corresponding value is the list of jumps
results ={}

print()
print("2019 Women's Triple Jump Final Results")
print()
# open the file
with open("triple_jump.csv") as data_file:
    # for each line in the file
    for line in data_file:
        # split each line into a list of components, but keep the jumps together
        values = line.strip().split(",", maxsplit=3)

        # for clarity, assigning the items in the values list to variables
        name = values[0]
        bib = values[1]
        country = values[2]

        # create a list of the jump distances, ignoring non-jumps
        jumps = [ float(x) for x in values[3].split(",") if float(x) != 0 ]

        print(f"{bib:>4} {name:18} ({country:3}) {jumps}")
        
        # insert into the dictionary
        # each competitor's name is associated with her list of jumps
        results[name] = jumps
        
# create a figure and an axis object
fig, ax = plt.subplots()

# set the labels on the axes
ax.set_xlabel("Distances")
ax.set_ylabel("Competitor")
# set the title
ax.set_title("2019 Women's Triple Jump Results")

# do a box plot
ax.boxplot(results.values(), vert=False, labels=results.keys())
plt.show() # display 

# save the image
fig.savefig('triple_jump_boxplot.png', bbox_inches='tight')



    





