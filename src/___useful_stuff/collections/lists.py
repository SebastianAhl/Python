"Information about Python Lists"
# List methods: https://www.w3schools.com/python/python_lists_methods.asp

# Overview collections in Python:
# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.

print("\n")
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
print("\nCheck for item in the list")
MySecList = ["123", "345", "678"]

if "345" in MySecList:
    print("it is in the list")


# change multiple items
print("\nChanged items in the list")
# if you add more items then indexed, they will be inserted
MyThirdList = ["abc", "def", "ghi"]
MyThirdList[1:2] = ["xyz", "qwert"]
print("Added more items then indexed:", MyThirdList)

# if you add less items then indexed, they will reduced
MyFourthList = ["abc", "def", "ghi"]
MyFourthList[1:3] = ["qwert"]
print("Added less items then indexed", MyFourthList)


# insert new items
MyFifthList = ["abc", "def", "ghi"]
MyFifthList.insert(1, "blub")
print("Inserted new item:", MyFifthList)


# insert new item at the end append()
MyFifthList.append("bla")
print("Inserted new item at the end:", MyFifthList)

# extend with another collection
MyFifthList.extend(MyList)
print("Extended one list with another list:", MyFifthList)


# remove item, only removes the first occurrence
print("\nRemoving data of the list")
MyFifthList.remove("blub")
print("Removed an item:", MyFifthList)

# removing of an specific index
MyFifthList.pop(0) # "abc"
print("Removed an item using index:", MyFifthList)

MyFifthList.pop() # last item "c"
print("Removed last item:", MyFifthList)

# with del
del MyFifthList[0] # "def"
print("Removed item using del:", MyFifthList)

# clear the data in the list, not delete the list
MyFifthList.clear()
print("Deleted everything in the list:", MyFifthList)

# deletes the list completely
del MyFifthList
print("Deleted the list completely!")
# print(MyFifthList) # --> list was deleted, Error

#############################################
# sort lists
# https://www.w3schools.com/python/python_lists_sort.asp
# case sensitive
print("\nSorting lists")
MySixthList = ["a", "x", "b", "5", "Z", "1", "c"]
print("Unsorted: ", MySixthList)
MySixthList.sort()
print("Sorted: ", MySixthList)

#############################################
# copy lists
# https://www.w3schools.com/python/python_lists_copy.asp
# list() method is possible as well as slice operator [:]
print("\nCopy a list")
ListToCopy = ["abc", "123"]
EmptyList = ListToCopy.copy()
print("Empty list after copying data (not empty anymore):", EmptyList)

#############################################
# Join lists
# use of operator +, method extend or append
print("\nJoin lists")
ListA = ["abc", "def"]
ListB = ["123", "345"]
ListOutput = ListA + ListB
print("Joined lists with + operator:", ListOutput)

# use of append
ListOutput.clear()
for X in ListA:
    ListOutput.append(X)

for X in ListB:
    ListOutput.append(X)

print("Appended items:", ListOutput)

# use of extend
ListOutput.clear()
ListOutput.extend(ListA)
ListOutput.extend(ListB)

print("Extended lists:", ListOutput)


#############################################
# Comprehension - shorter syntax, but more difficult to read
# https://www.w3schools.com/python/python_lists_comprehension.asp
print("\nComprehension:")
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# newlist = [expression for item in iterable if condition == True]
# for x in fruits:
#   if "a" in x:
#     newlist.append(x)
newlist = [x for x in fruits if "a" in x]

print(newlist)
