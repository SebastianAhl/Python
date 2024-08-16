"How to loop collections"
# a lot of examples:
# https://www.w3schools.com/python/python_lists_loop.asp
# https://www.w3schools.com/python/python_tuples_loop.asp
# https://www.w3schools.com/python/python_sets_loop.asp
# https://www.w3schools.com/python/python_dictionaries_loop.asp

# looping every item (same for all collections)
MyList = ["abc", "123", "def", "456"]
MyDict = {
    "letters": "abc",
    "numbers": 123
}

print("\nEasy printing list items:")
for X in MyList:
    print(X)

print("\nEasy printing dict values:")
for X in MyDict:
    print(MyDict[X])


# indexed looping lists, tuples
print("\nWith range: ")
for I in range(len(MyList)):
    print(MyList[I])

# recommended
print("\nWith enumerate: ")
for I, ListObject in enumerate(MyList):
    print(I, ListObject)
