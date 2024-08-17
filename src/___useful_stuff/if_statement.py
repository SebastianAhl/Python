"Python if statement"

# Equals:                       a == b
# Not Equals:                   a != b
# Less than:                    a < b
# Less than or equal to:        a <= b
# Greater than:                 a > b
# Greater than or equal to:     a >= b

# 'and', 'or', 'not' keywords can be used


print("\nPython if statement")

# Basic if statement
print("\nBasic if statement")
A = 1
B = 1
C = 10

if A == B:
    print("A == B")

# if A == B: print("A == B") # works too, but not nice


# elif statement
print("\nelif statement")
if A < B:
    print("A < B")
elif A == B:
    print("A == B")


# if else statement
print("\nif else statement")
if A < B:
    print("A < B")
elif A > B:
    print("A > B")
else:
    print("A is not <> B")

# print("A < B") if A < B else print("A is not < B") # works too, but not nice


# pass statement
# rarely used because you will only need it in an empty if statement
print("\npass statement")
if A == B:
    pass
