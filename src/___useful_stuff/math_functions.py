"Examples of math functions"

# There are different built-in (meaning: no need to import) math functions in python
# Furthermore there is a math module in python (import math) with further math functions

print("\n##### integrated math functions #####")
# min() max() functions return smallest and biggest value
print("\nmin() max() functions:")
print("min():", min(10, 1, 2, 3, 20, 15))
print("max():", max(10, 1, 2, 3, 20, 15))


# abs() function returns absolute value of a number
print("\nabs() function:")
print("abs(-2.4567):", abs(-2.4567))


# pow() function returns the value of a number x to the power of y --> x^y
print("\npow() function:")
print("pow(2, 0):", pow(2, 0))
print("pow(2, 1):", pow(2, 1))
print("pow(2, 2):", pow(2, 2))


####################################
####################################
# math module
import math
print("\n##### math module #####")

# math.sqrt()
print("\nmath.sqrt() function returns the square root of a number")
print("math.sqrt(16):", math.sqrt(16))


# math.ceil() and math.floor()
print("\nmath.ceil() rounds upwards, math.floor() round downwards")
print("math.ceil(4.1):", math.ceil(4.1))
print("math.floor(4.9):", math.floor(4.9))


# math.pi returns pi
print("\n math.pi() returns pi")
print("math.pi):", math.pi)
