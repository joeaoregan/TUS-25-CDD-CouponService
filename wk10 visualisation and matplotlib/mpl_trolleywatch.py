"""
Program to visualise Trolley Watch data with a histrogram, box plot and violin plot
Example of: Visualisation with matplotlib
(For simplicity, ignoring errors, i.e. no Exception Handling)

"""
import matplotlib.pyplot as plt

# create a list for the patients numbers
patients_list = []

# read the data from the file
with open("examples/trolleywatch3.csv") as data_file:
    # read the first line containing the headings and discard it
    data_file.readline()
    
    # for each other line in the file
    for line in data_file:
        # split the line into the components
        date_string, hospital, region, trolley, ward, patients = line.strip().split(",")

        # add to the list
        patients_list.append(int(patients))


# Create the figure and axes
fig, axs = plt.subplots(1,3)
# Set the title for the figure
fig.suptitle("Trolleywatch Visualisations")
# 1 histogram
# Set the title
axs[0].set_title("Histogram")
# set the axis labels
axs[0].set_xlabel("Patients")
axs[0].set_ylabel("Frequency")
# create a list for the bins (histogram boundaries)
# bins = range(0, 100, 10)
# axs[0].set_xticks(bins)
# Display a histogram of the patient numbers
axs[0].hist(patients_list,edgecolor="black") #, bins, edgecolor

# 2. Box plot
# Set the title
axs[1].set_title("Box Plot")
# Set the y axis label
axs[1].set_ylabel("Patients")
# Display a box plot of the patients numbers
axs[1].boxplot(patients_list, showmeans=True) #, showfliers=False


# 3. Violin
# Set the title
axs[2].set_title("Violin Plot")
# set the y  axis label
axs[2].set_ylabel("Patients")
# Display a violin plot of the patients numbers
axs[2].violinplot(patients_list, showmeans=True)

# show the plot
plt.show()
# save the figure
fig.savefig("trolleywatch.png")