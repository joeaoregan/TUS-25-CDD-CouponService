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

# display the histogram, using the default number of bins (10)
ax.hist(magnitudes) # same as using keyword argument bins=10

# show the figure (not required with Spyder)
plt.show()

