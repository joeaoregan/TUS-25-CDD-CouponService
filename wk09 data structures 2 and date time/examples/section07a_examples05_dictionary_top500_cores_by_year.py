# Program to determine the Year with the Highest Average Total Cores
# Example of a dictionary with a list as the value for each key
with open("TOP500_202506.csv") as top500_file:
    # Read and ignore the first line (headings)
    _ = top500_file.readline()

    # Start with an empty dictionary
    cores_per_year = {}

    # Process each line in the file
    for line in top500_file:
        # only interested in the year and total_cores values
        _, _, _, _, year, _, total_cores, _ = line.strip().split(",")
        
        # append the total_cores to the lit for the year on this line
        # if the year hasn't been encountered yet, then start with an empty list
        

        cores_per_year.setdefault(year, []).append(int(total_cores))

# a) Year with the most supercomputers
# The number of supercomputers per year is the length of each list
year_most_supercomputers = max(cores_per_year, key=lambda y: len(cores_per_year[y]))
num_supercomputers = len(cores_per_year[year_most_supercomputers])
print(f"Year with the most supercomputers: {year_most_supercomputers} ({num_supercomputers} systems)")

# b) Year with the highest average total cores
# Calculate average cores per year
average_cores_per_year = { year: sum(cores)/len(cores) for year, cores in cores_per_year.items() }

# determine year with highest average
year_highest_avg_cores = max(average_cores_per_year, key=average_cores_per_year.get)
highest_avg = average_cores_per_year[year_highest_avg_cores]
print(f"Year with the highest average total cores: {year_highest_avg_cores} ({highest_avg:.0f} cores per system)")

