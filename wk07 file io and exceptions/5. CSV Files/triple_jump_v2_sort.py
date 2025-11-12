# Purpose: Find the winnner of the Triple Jump competition
# Example of: File input from a csv file, splitting using maxsplit parameter, using nested lists

athletes = []  # outer list to store all athletes' data

# open the file
with open("TripleJump.csv") as data_file:
    # for each line in the file
    for line in data_file:
        try:
            # split into componenets: name, bib, country, and the jumps
            name, bib, country, jump_values = line.strip().split(",", maxsplit=3) # maxsplit has to happen at the end
        except:
            print(f"Invalid format in line: {line.strip()}")
        else:
            try:
                # create a list of jump distances (as floats)
                jumps = [float(x) for x in jump_values.split(",")]
            except ValueError:
                print(f"Invalid jump value(s) in line: {line.strip()}")
            else:
                # store all athlete data in a nested list
                athletes.append([name, bib, country, jumps])

# Sort the athletes by best jup (highest first)
athletes.sort(key=lambda athlete: max(athlete[3]), reverse=True)

print("Women's Triple Jump Final Results\n")
print(f"{'Bib':>5} {'Name':28} Best Jump")
for athlete in athletes:
    # print(f"{athlete[1]:>5} {athlete[0]:20} ({athlete[2]:3}) {max(athlete[3]):>7.2f}")
    name, bib, country, jumps = athlete
    best_jump = max(jumps)
    print(f"{bib:<5} {name:20} ({country}) {best_jump:>7.2f}")
