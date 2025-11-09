# Shelves as Persistent Dictionaries
# shelve provides persistent data storage using dictionary-like object
# * Keys must be strings
# * Values can be any pickable Python object           (Pickling: storing Python objects in a file)
#      (number, strings, lists, dictionaries, etc.)
# * The data is automatically stored in a file on disk.

# import: import shelve
# Open (existing or creates new file):
#     with shelve.open("data.db") as data:
# automatically hadnles file opening and closing safely

# There are certain things that can't be pickled