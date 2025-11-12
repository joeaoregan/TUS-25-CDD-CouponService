# Dictionary for Grouping Values

# Group Total Cores values by year

with open("TOP500_202506.csv") as top500_file:
    # Read and ignore the first line (headings)
    _ = top500_file.readline()

    # Start with an empty dictionary
    cores_per_year = {}

    # Process esach line in the file
    for line in top500_file:
        # only interested in the year and total_cores values
        _, _, _, _, year, _, total_cores, _ = line.strip().split(",")

        # append the total_cores to the list for the year on this line
        # if the year hasn't been encountered yet, then start with an empty list
        # .setdefault(year, []) ensures that each year has a list to append the Total Cores to:
        cores_per_year.setdefault(year, []).append(int(total_cores))
    
    # print(cores_per_year)
    # Year with most supercomputers is Year with longest list (of Total Cores)
    year_most_sueprcomputers = max(cores_per_year, key=lambda y: len(cores_per_year[y])) # Calculated using a lambda as the key function for max()
    num_supercomputers = len(cores_per_year[year_most_sueprcomputers])
    print(f"Year with the most supercomputers: {year_most_sueprcomputers} ({num_supercomputers} systems)")

    # Calculate the average Total Cores each Year (dictionary comprehension):
    average_cores_per_year = { year: sum(cores) / len(cores) for year, cores in cores_per_year.items()}

    # Year with the highest average: max(key=dict.get)
    year_highest_avg_cores = max(average_cores_per_year, key=average_cores_per_year.get)    
    print(f"Year with the highest average total cores: {year_highest_avg_cores} ({average_cores_per_year[year_highest_avg_cores]} cores per system)")
    # print(year_highest_avg_cores)



