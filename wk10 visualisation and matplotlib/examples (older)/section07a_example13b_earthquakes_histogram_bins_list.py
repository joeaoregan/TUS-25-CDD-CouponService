# Import the matplotlib
import matplotlib.pyplot as plt

# Create an empty dictionary called earthquakes
magnitudes = []
# Open the file
with open("earthquakes_2019.csv") as data_file:
    # Read in the headers line
    _ = data_file.readline()
    # For each line in the file
    for line in data_file:
        # Split the line into 
        date_string, latitude, longitude, magnitude, place = line.split(",",maxsplit=4)
        
        # Add the magnitude value to the list
        magnitudes.append(float(magnitude))
        
# Create the figure and axes
fig, ax = plt.subplots()

# Set the title
ax.set_title("Earthquakes Histogram")
# set the axis labels
ax.set_xlabel("Magnitude")
ax.set_ylabel("Number of Earthquakes")

# specify the bins using a list
# this list will be 0, 0.5, 1.0, 1.5, ... and will include the maximum magnitude
bins_list = [ i/2 for i in range(int(max(magnitudes))*2+1)]

# set the tick marks on the x-axis to correspond with the bins
ax.set_xticks(bins_list)

# display the histogram, specifying the bins using a list
ax.hist(magnitudes, bins=bins_list, ec="black") # set the edge colour to black

# show the figure (not required with Spyder)
plt.show()

