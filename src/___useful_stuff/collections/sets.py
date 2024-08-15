"Information about Python Sets"
# List methods: https://www.w3schools.com/python/python_sets_methods.asp

# Overview collections in Python:
    # List is a collection which is ordered and changeable. Allows duplicate members.
    # Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
    # Dictionary is a collection which is ordered** and changeable. No duplicate members.

# unchangeable means, set items cannot be changed, but you can remove items and add new items!!!
# no dublicates are allowed --> True == 1 and False == 0
# a set has no index [INT]
# a set can contain different data types


print("\nPython Sets")

# Declaration of a set
MyFirstSet = {"abc", 123, True, 456, False, "def"}
print("Declaration of a set:", MyFirstSet)

# Accessing a set
print("\nAccessing a set")

# Looping
print("With for-loop:")
for X in MyFirstSet:
    print(X)

# Checking
print("Check if a value is in the set")
print("'abc' is in the set --> True:", "abc" in MyFirstSet)
print("'abc' is not in the set --> False:", "abc" not in MyFirstSet)


# Add an item
print("\nAdd an item")

MyFirstSet.add("qwertz")
print("'qwertz' was added:", MyFirstSet)


# Add a collection to a set
print("\nAdd a set to a set")
MySecSet = {"blub", "bla", 14684654}

MyFirstSet.update(MySecSet)
print("'blub', 'bla', 14684654 were added to the set:", MyFirstSet)


# Remove set items remove()
print("\nRemove set items with remove()")

MyFirstSet.remove("qwertz")
print("'qwertz' was removed:", MyFirstSet)

print("Raises an error if item doesn't exist: Uncomment next line and you will see")
# MyFirstSet.remove("qwertz")


# Remove set items discard()
print("\nRemove set items with discard()")

MyFirstSet.discard("qwertz")
print("'qwertz' was discarded:", MyFirstSet)

print("Raises no error if item doesn't exist: Or do you see any error in the next output line in the terminal?")
MyFirstSet.discard("qwertz")


# Remove a random item with pop()
print("\nRemove a random item with pop()")

print("Before pop():", MyFirstSet)
MyFirstSet.pop()
print("After pop(): ", MyFirstSet)


# Empty a set with clear()
print("\nEmpty a set with clear()")
SetToClear = {""}
SetToClear.update(MyFirstSet)

print("Before clear():", SetToClear)
SetToClear.clear()
print("After clear(): ", SetToClear)


# Delete a set completly with del keyword
print("\nDelete a set completly with del()")
SetToDelete = {""}
SetToDelete.update(MyFirstSet)

print("Before del():", SetToDelete)
del SetToDelete
print("Accessing the set to print it would couse an error. Try by uncommenting next line.")
# print("After del(): ", SetToDelete)


# Joining sets
# https://www.w3schools.com/python/python_sets_join.asp
# There are several ways to join two or more sets in Python.
#     The union() and update() methods joins all items from both sets.
#     The intersection() method keeps ONLY the duplicates.
#     The difference() method keeps the items from the first set that are not in the other set(s).
#     The symmetric_difference() method keeps all items EXCEPT the duplicates.