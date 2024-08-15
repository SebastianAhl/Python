"How to loop collections"
# a lot of examples:
# https://www.w3schools.com/python/python_lists_loop.asp

# looping every item (same for all collections)
MyList = ["abc", "123", "def", "456"]

for X in MyList:
    print(X)


# indexed looping
print("\nWith range: ")
for I in range(len(MyList)):
    print(MyList[I])

# recommended
print("\nWith enumerate: ")
for I, ListObject in enumerate(MyList):
    print(I, ListObject)
