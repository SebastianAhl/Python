"Some examples for string formatting with F-String"

# source: https://www.w3schools.com/python/python_string_formatting.asp
    # for more Formatting Types just search on the website for Formatting types

# Used to format strings
# Before Python 3.6 format() function had to used. More information on the website.
# In this document I only talk about the F-Strings

print("\nF-Strings")
# basic syntax
print("\nBasic Syntax")

TEXT = f"Hello World 2024!"
print(TEXT)

##############
print("\nPlaceholders {}")
YEAR = 2025

TEXT = f"Hello World {YEAR}!"
print(TEXT)

##############
print("\nPlaceholders with modifier")
YEAR = 2025

TEXT = f"Hello World {YEAR:.2f}!"
print(TEXT)


##############
print("\nModifier")

print(f"just a modifier for to add 2 decimal places to the number 2: {2:.2f}")

print(f"2 * 5 = {2 * 5}")

AMOUNT = 10

print(f"Is AMOUNT bigger or smaller/equal then 10: {"Smaller/Equal" if AMOUNT <= 10 else "Bigger"}")

SMALL_LETTERS = "abcd"
print(f"Functions inside strings. Write {SMALL_LETTERS} in capital letters: {SMALL_LETTERS.upper()}")
