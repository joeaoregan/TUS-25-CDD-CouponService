# Purpuse: To analyse the word lengths in the file 'alice.txt'
# Example of: File input using read with exception handling
# filename = "alice.txt"
# filename = "D:\\TUS Python\\wk7 Exceptions and File Handling\\4. File Input\\alice.txt"
filename = "\\home"

try:
    with open(filename) as book_file:
        # read in the entire contents of the file as a string
        contents = book_file.read()
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
except PermissionError:
    print(f"Error: You do not have permission to read '{filename}'.")
except OSError as e:
    print(f"Unexpected file-related error: {e}")
else:
    # count number of words by splitting the contents into a list of words
    print("Number of words:", len(contents.split()))
    
    # count number of lines by splitting the contents into a list of lines
    print("Number of lines:", len(contents.splitlines()))

    # How many times does the word "Alice" appear?
    print("Occurences of 'Alice':", contents.count("Alice"))