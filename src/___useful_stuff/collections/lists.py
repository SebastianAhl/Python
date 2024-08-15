"Information about Python Lists"
# Overview collections in Python:
# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.


# objects of the class list
# used to store multiple items
# items are ordered, changeable and allow duplicate values
MyList = ["a", "b", "c"]

print("Print the whole list: ", MyList)

print("Length of list: ", len(MyList))


# list items can be indexed with [INT] or [-INT] or [INT:INT] or [-INT:-INT]
print("The first item in the list: ", MyList[0])

MyList[0] = "changed"
print("The first item in the list: ", MyList[0])


# check for specific item
MySecList = ["123", "345", "678"]

if "345" in MySecList:
    print("it is in the list")


# change multiple items
# if you add more items then indexed, they will be inserted
MyThirdList = ["abc", "def", "ghi"]
MyThirdList[1:2] = ["xyz", "qwert"]
print(MyThirdList)

# if you add less items then indexed, they will reduced
MyFourthList = ["abc", "def", "ghi"]
MyFourthList[1:3] = ["qwert"]
print(MyFourthList)


# insert new items
MyFifthList = ["abc", "def", "ghi"]
MyFifthList.insert(1, "blub")
print(MyFifthList)
