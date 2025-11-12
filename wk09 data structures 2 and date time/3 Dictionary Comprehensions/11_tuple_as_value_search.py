# Dictionary with tuple as value
# Example: Supercomputers
# Key: System ID (unique, string)
# Value: Tuple containing all attributes

with open("TOP500_202506.csv") as top500_file:
    # Read and ignore the first line (headings)
    _ = top500_file.readline()

    # Start with an empty dictionary
    supercomputers = {}

    # Process esach line in the file
    for line in top500_file:
        # only interested in the year and total_cores values
        system_id, name, manufacturer, country, year, segment, total_cores, rmax = line.strip().split(",")

        # insert into the dictionary
        # supercomputers[system_id] = (name, manufacturer, country, int(year), segment, int(total_cores), float(rmax))
        supercomputers[system_id] = (
            name,               # System name
            manufacturer,       # Manufacturer
            country,            # Country
            int(year),          # Year
            segment,            # Segment
            int(total_cores),   # Total cores
            float(rmax)         # Rmax (peak performance)
        )
    
    # a) System with the highest Rmax
    top_system_id = max(supercomputers, key=lambda sid: supercomputers[sid][6]) # System with highest Rmax determined using Lambda key funciton with max(). sid is the System ID, supercomputers[sid][6] retrieves Rmax for each sid key
    name, manufacturer, country, year, segment, total_cores, rmax = supercomputers[top_system_id]

    # print("\nSystem with highest Rmax:")
    # print(f"ID: {top_system_id}")
    # print(f"Name: {name}")
    # print(f"Manufacturer: {manufacturer}")
    # print(f"Country: {country}")
    # print(f"Year: {year}")
    # print(f"Segment: {segment}")
    # print(f"Total cores: {total_cores}")
    # print(f"Rmax: {rmax:.2f} petaflops")

    while True:
        search_country = input("\nEnter a country to search (or press Enter to quit): ").strip()
        if not search_country:
            print("Goodbye!")
            break

        found = False
        for sid, (name, manufacturer, country, year, segment, total_cores, rmax) in supercomputers.items():
            if country.lower() == search_country.lower():
                print(f"{year}: {name} ({manufacturer}) - {total_cores:,} cores, {rmax:.2f} petaflops")
                found = True

        if not found:
            print(f"No entries found for {search_country}.")
