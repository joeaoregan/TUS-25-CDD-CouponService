"""
Program to visualise Trolley Watch data with a histrogram, box plot and violin plot
Example of: Visualisation with matplotlib
(For simplicity, ignoring errors, i.e. no Exception Handling)

"""
import matplotlib.pyplot as plt

# create a list for the patients numbers
patients_list = []

# read the data from the file
with open("trolleywatch3.csv") as data_file:
    # read the first line containing the headings and discard it
    data_file.readline()
    
    # for each other line in the file
    for line in data_file:
        # split the line into the components
        date_string, hospital, region, trolley, ward, patients = line.strip().split(",")
        
        # add to the list
        patients_list.append(int(patients))

        
# Create the figure and axes

# Set the title for the figure
# 1 histogram    
# Set the title

# set the axis labels


# create a list for the bins (histogram boundaries)

# set the ticks on the x-axis

# Display a histogram of the patient numbers


# 2. Box plot
# Set the title

# set the y axis label

# Display a box plot of the patients numbers


# 3. Violin plot 
# Set the title

# set the y axis label

# Display a violin plot of the patients numbers


# show the plot

# save the figure


