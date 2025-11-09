# Program Name: section06_example07_scatterplot.py
# Purpose: To plot the performances of supercomputers
# Example of: matplotlib scatter plot

import matplotlib.pyplot as plt

# create empty lists for the data
x_cores = []
y_rmax = []

# read the data from the file
with open("TOP500_201906.csv") as datafile:
    # read the headers line
    headers = datafile.readline()    
    
    # for each line in the file
    for line in datafile:        
        # split the line into the components
        rank, name, cores, rmax, rpeak  = line.strip().split(",")
        
        # insert into lists        
        x_cores.append(int(cores))
        y_rmax.append(float(rmax))
        

# create a figure and an axis object
fig, ax = plt.subplots()

# set the labels on the axes
ax.set_xlabel("Total Cores")
ax.set_ylabel("Rmax (TFlops)")

# set the title
ax.set_title("Top 500 Supercomputers")

# do a scatter plot
ax.scatter(x_cores, y_rmax, marker=".")
plt.show()

# save the image
fig.savefig('scatterplot_supercomputers.png', bbox_inches='tight')


