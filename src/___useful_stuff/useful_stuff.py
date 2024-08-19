"Useful stuff"
print("\nUselful stuff")
#########################
# Return datatype with type()
print("\ntype()")

X = ("abc")
Y = (3)
Z = float(3.123)

print("X: ", type(X))
print("Y: ", type(Y))
print("Z: ", type(Z))


#########################
# Random numbers
import random
print("\nimport random")

print("Random number:", random.randrange(1, 1000, step=1))


#########################
# Check if it is an instance with isinstance()
print("\nisinstance()")

X = 200
print("Is it an instance?", isinstance(X, int))


#########################
# Using datetime
print("\nimport datetime")

import datetime
X = datetime.datetime.now()

print("Date and time:", X)

print("Formating the datetime with strftime()")
# formating strings: https://www.w3schools.com/python/python_datetime.asp
print("Formated date and time:", X.strftime("%B"))
