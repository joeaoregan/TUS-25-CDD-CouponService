filename = input("Enter the filname: ")

try:
    with open(filename) as top500_file:
        # Read and ignore the first line (headings)
        headings = top500_file.readline()

        # To find the max, start with 0 and look for a higher value
        top_system = None
        top_rmax = 0.0

        # Process each line in the file
        for line in top500_file:
            try:
                system_id, name, manufacturer, country, year, segment, total_cores, rmax = line.strip().split(",")
                rmax = float(rmax) # convert to decimal

                # Update if this system has a higher Rmax
                if rmax > top_rmax:
                    top_rmax = rmax
                    top_system = name
                
            except ValueError:
                print(f"Skipping malformed line: {line.strip()}")
    
    # after successful processing
    print(f"Top Supercomputer: {top_system}")
    print(f"Rmax Value: {top_rmax}")

except FileNotFoundError:
    print(f"File not found: {filename}")
except PermissionError:
    print(f"No permission to read file: {filename}")
except OSError as e:
    print(f"Unexpected file-related error: {e}")