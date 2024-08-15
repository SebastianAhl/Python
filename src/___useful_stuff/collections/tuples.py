"Information about Python Tuples"
# List methods: https://www.w3schools.com/python/python_tuples_methods.asp

# Overview collections in Python:
    # List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
    # Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
    # Dictionary is a collection which is ordered** and changeable. No duplicate members.

# unchangeable means, cannot delete/ add/ change items after creation!!!
# a tuple can contain different data types

print("\nPython Tuples")

# declaration of a tuple
MyFirstTuple = ("abc", "def", "123")

print("My first tuple:", MyFirstTuple)


# tuples can be accessed with the index [INT] [-INT] [INT:INT] [-INT:-INT]
print("\nValue at index 1 --> 'def':", MyFirstTuple[1])


# check if a keyword is present in a tuple
print("Is 'abc' in the tuple?:", "abc" in MyFirstTuple)
print("Is 'abc' not in the tuple?:", "abc" not in MyFirstTuple)


# tuple with only one item needs a comma "," otherwise it is no tuple
TupleWithOneValue = ("one value", )
print("\nTuple with only one value:", TupleWithOneValue)


# tuples with different data types
MySecTuple = ("abc", 123, "def", True, 456)
print("\nTuple with different data types:", MySecTuple)


# unpacking tuples in variables, variables must match values in tuple or use of *
print("\nUnpacking a tuple in variables")
MyClothes = ("Tshirt", "Jeans", "Socks", "Jacket", "Pullover")

(white, blue, black, green, grey) = MyClothes

print("Variable white --> Tshirt:", white)
print("Variable blue --> Jeans:", blue)
print("Variable black --> Pullover:", black)

(white, *blue, grey) = MyClothes
print("Variable white --> Tshirt:", white)
print("Variable blue --> List ['Jeans', 'Socks', 'Jacket']:", blue)
print("Type of blue:", type(blue))
print("Variable blue --> Pullover:", grey)


# Join tuples
print("\nJoining tuples")
MyTuple1 = ("abc", "def", "ghi")
MyTuple2 = (123, 456, 789)

JoinedTuple = MyTuple1 + MyTuple2

print("Joined new tuple:", JoinedTuple)


# Multiply tuples
print("\nMultiply tuples")
DoubledTuple = MyTuple1 * 2
TrippledTuple = MyTuple1 * 3

print("Doubled tuple:", DoubledTuple)
print("Trippled tuple:", TrippledTuple)
