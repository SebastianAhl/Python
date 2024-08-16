"Information about Python Dictionaries (DICT)"
# List methods: https://www.w3schools.com/python/python_dictionaries_methods.asp

# Overview collections in Python:
    # List is a collection which is ordered and changeable. Allows duplicate members.
    # Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
    # Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.

# changeable means, set items can be changed
# dublicates are not allowed
# dictionaries are order since Python 3.7 --> not sorted
# values can be accessed by their keys


# a set can contain different data types

print("\nStuff about Dictionaries (DICT)")

# example of a dict
MyFirstDict = {
    "brand": "apple", # "KEY": "VALUE"
    "model": "iphone",
    "Price": 1000
}

print("My first dict:", MyFirstDict)


# Access the value of a key
print("\nAccess the value of a key")
print("Directly:", MyFirstDict["brand"])

X = MyFirstDict["brand"]
print("By copying it in a variable:", X)

print("With get():", MyFirstDict.get("brand"))


# Get lists
print("\nGet lists")
print("All values:", MyFirstDict.values())

print("All keys:", MyFirstDict.keys())

X = MyFirstDict.items()
print("All items in tuples:", X)


# Check if a key exists
print("\nCheck if the key 'model' exists --> True:", "model" in MyFirstDict)
print("Check if the key 'model' not exists --> False:", "model" not in MyFirstDict)


# Checking the dict lenght with len()
print("\nChecking the dict lenght/number of items:", len(MyFirstDict))


# Adding a new item
print("\nAdding a new item")
print("Before change:", MyFirstDict.keys())

MyFirstDict["color"] = "grey"
print("After change directly:", MyFirstDict.keys())

MyFirstDict.update({"material": "aluminium"})
# if the key does not exist, update will create it
print("After change with update:", MyFirstDict.keys())


# Changing values of items
print("\nChanging values of items")

print("Changing a single item directly")
print("Before change Price = 1000:", MyFirstDict["Price"])
MyFirstDict["Price"] = 500
print("After change Price = 500:", MyFirstDict["Price"])

print("Changing with use of update()")
MyFirstDict.update({"Price": 750})
print("Used update to change Price = 750:", MyFirstDict["Price"])


# Copy dicts
print("\n Copy dicts")
MyCopyDict = MyFirstDict.copy()
print("Original MyFirstDict :", MyFirstDict)
print("A copy of MyFirstDict:", MyCopyDict)


# Removing items
print("\nRemoving items")
MyFirstDict.pop("material")
print("An item with its key and pop():", MyFirstDict.keys())

MyFirstDict.popitem()
print("The last item with popitem():", MyFirstDict.keys())

del MyFirstDict["model"]
print("An item with its key and del:", MyFirstDict.keys())

MyFirstDict.clear()
print("Emptying the whole dict with clear():", MyFirstDict.keys())

del MyFirstDict
print("Deleted the whole dict with del")


# Nested dicts
print("\nCreate nested dicts")
MobilePhones1 = {
    "Phone1": {
        "brand" : "apple",
        "model" : "iphone"
    },
    "Phone2": {
        "brand" : "samsung",
        "model" : "z4"
    },
    "Phone3": {
        "brand" : "sony",
        "model" : "experia"
    }
}

# or

Phone1 = {
        "brand" : "apple",
        "model" : "iphone"
}

Phone2 = {
        "brand" : "samsung",
        "model" : "z4"
}

Phone3 = {
    "brand" : "sony",
    "model" : "experia"
}

MobilePhones2 = {
    "Phone1" : Phone1,
    "Phone2" : Phone2,
    "Phone3" : Phone3
}

print("\nAccess nested dicts")
print("Direct access to one item:", MobilePhones1["Phone1"]["brand"])

print("\nLooping...")
for x, obj in MobilePhones1.items():
    print(x)

    for y in obj:
        print(y + ':', obj[y])
