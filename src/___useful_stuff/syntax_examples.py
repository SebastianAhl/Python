"Syntax examples"
#########################
# Comments
# Ctrl + # --> fast (un)comment full line or multiple lines

print("Hello World") # Comment

"""
Multiline --> not official
Multiline
Multiline
"""

#########################
# Variable declaration and access

X = 5
print(X)

X = "Hello World"
print(X)

X = str("abc")
Y = int(3)
Z = float(3.1234)

X, Y, Z = "Orange", "Banana", "Cherry"
print(X, Y, Z)

X = Y = Z = "Orange"
print(X, Y, Z)

# Collections
# Unpack
fruits = ["apple", "banana", "cherry"]
X, Y, Z = fruits
print(X)
print(Y)
print(Z)
