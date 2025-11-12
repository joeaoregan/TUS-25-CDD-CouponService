# Program to determine the top Supercomputer from the Top 500

# Determine the top supercomputer by Rmax value

# filename = "TOP500_202506.csv"
filename = "TOP500_202506_2.csv" # file with errors

try:
    with open(filename) as top500_file:
        # Read and ignore the first line (headings)
        # top500_file.readline() # works fine but, using _ makes it clearer
        _ = top500_file.readline()

        # To find the max, start with 0 and look for a higher value
        top_name = None
        top_rmax = 0.0

        # Process each line in the file
        for line in top500_file:
            # --- Step 1: Split line safely ---
            try:
                _, name, _, _, _, _, _, rmax = line.strip().split(",")
                rmax = float(rmax) # convert to decimal
            except ValueError:
                print(f"Skipping malformed line: {line.strip()}")

            # --- Step 2: Convert Rmax safely ---
            try:
                rmax_value = float(rmax)
            except ValueError:
                print(f"Skipping line (invalid Rmax value): {rmax}")
                continue

            # --- Step 3: Compare with current top system ---
            if rmax_value > top_rmax:
                top_rmax = rmax_value
                top_name = name
                
    
        print()
        print(f"Top Supercomputer: {top_name}")
        print(f"Rmax Value: {top_rmax:,.2f}")

except FileNotFoundError:
    print(f"File not found: {filename}")
except PermissionError:
    print(f"No permission to read file: {filename}")
except OSError as e:
    print(f"Unexpected file-related error: {e}")