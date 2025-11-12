# Purpose: Processing data in a CSV file
# Example of: Robust Exception Handling

fires_list = []  # starts with an empty list
valid_file = False

while not valid_file:  # keep prompting until a valid file is entered
    filename = input("Enter the filename: ")
    try:
        with open(filename, encoding="latin-1") as data_file:
            # Read and ignore the header line
            _ = data_file.readline()
            for line in data_file:
                try:
                    # remove newline and split into components
                    _, _, _, fires, _ = line.strip().split(",")

                    # convert fires to integer and append to 
                    fires_list.append(int(fires))
                except ValueError:
                    print(f"Skipping invalid line: {line.strip()}")

        valid_file = True # file opened and processed successfully

    except FileNotFoundError:
        print(f"File not found: {filename}")
