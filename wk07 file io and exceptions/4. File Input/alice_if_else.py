import os

filename = "D:\\TUS Python\\wk7 Exceptions and File Handling\\4. File Input\\alice.txt"

with open(filename) as book_file:
    # read in the entire contents of the file as a string
    contents = book_file.read()

# Check if the file exists
if os.path.exists(filename):
    # Check if it is a file (not a directory)
    if os.path.isfile(filename):
        # Check if we have permission to read the file
        if os.access(filename, os.R_OK):
            # Attempt to open and read the entire file as a string
            with open(filename) as book_file:
                # read in the entire contents of the file as a string
                contents = book_file.read()

                # count number of words by splitting the contents into a list of words
                print("Number of words:", len(contents.split()))
                
                # count number of lines by splitting the contents into a list of lines
                print("Number of lines:", len(contents.splitlines()))

                # How many times does the word "Alice" appear?
                print("Occurences of 'Alice':", contents.count("Alice"))
        else:
            print(f"Error: No permission to read the file '{filename}'.")
    else:
        print(f"Error: '{filename}' is a directory")
else:
    print(f"Error: The file '{filename} does not exist")