# Purpose: To analyse the word lengths in the file 'alice.txt'
# Example of: file input using read

with open("D:\\TUS Python\\wk7 Exceptions and File Handling\\4. File Input\\alice.txt") as book_file:
    # read in the entire contents of the file as a string
    contents = book_file.read()

    # count number of words by splitting the contents into a list of words
    print("Number of words:", len(contents.split()))
    
    # count number of lines by splitting the contents into a list of lines
    print("Number of lines:", len(contents.splitlines()))

    # How many times does the word "Alice" appear?
    print("Occurences of 'Alice':", contents.count("Alice"))