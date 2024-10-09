"Examples on how to handle files"

# open() command
# "r" Read
# "a" Append or create
# "w" Write or create
# "x" Create

# handle as:
# "t" Text
# "b" Binary --> e.g. pictures

print("Opening file")

doc = open(r"src\___useful_stuff\file_handling\textfile.txt", "rt", encoding="utf-8")
# r"string" is used to ignore the escape characters
# https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/anomalous-backslash-in-string.html
# "rt" is standard
# encoding can easily found out it windows by opening the file with Notepad,
# using "save as" and on the right side bottom is the encoding listet

print("\nPrint 3 characters of the file:")
print(doc.read(3))

print("\nPrint the rest of the first line and the second line of the file:")
print("Rest:", doc.readline())
print("Second:", doc.readline())

print("\nClose the file")
doc.close()

#############################
print("\nPractice writing to files")

trashfile = open(r"src\___useful_stuff\file_handling\trash.txt", "w", encoding="utf-8")
trashfile.write("Trash")
trashfile.close()

trashfile = open(r"src\___useful_stuff\file_handling\trash.txt", "r", encoding="utf-8")
print(trashfile)

trashfile.close()

#############################
print("\nDelete files")
import os # I know this is not the right place for an import :-)

os.remove(r"src\___useful_stuff\file_handling\trash.txt")
