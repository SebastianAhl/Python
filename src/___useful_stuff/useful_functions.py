"Useful functions"
#########################
# Return datatype with type()

X = ("abc")
Y = (3)
Z = float(3.123)

print("X: ", type(X))
print("Y: ", type(Y))
print("Z: ", type(Z))

# Random numbers
import random

print(random.randrange(1, 1000, step=1))

# Check the datatype with isinstance()
x = 200
print(isinstance(x, int))
