# Purpose: Find the winnner of the Triple Jump competition
# Example of: File input from a csv file, splitting using maxsplit paramter, 
print("Women's Triple Jump Final Results\n")

# open the file
with open("TripleJump.csv") as data_file:
    # headings for output
    print(f"{'Bib':>4} {'Name':24} Best Jump")

    # for each line in the file
    for line in data_file:
        try:
            # split into componenets: name, bib, country, and the jumps
            name, bib, country, jump_values = line.strip().split(",", maxsplit=3) # maxsplit has to happen at the end

            try:
                # create a list of jump distances
                jumps = [float(x) for x in jump_values.split(",")]
                print(f"{bib:>4} {name:18} ({country:3}) {max(jumps):>7.2f}")

            except ValueError:
                print(f"Error: Non-numeric value found in jump distance for {name}")

        except ValueError:
            print(f"Error: Incorrect forma in line - {line.strip()}")