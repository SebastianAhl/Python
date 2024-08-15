"Stuff about Strings"

# Inside quotes
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

# Multiline
A = """First line,
line2,
line3
last line."""
print(A)

# Concatenate
A = "Part1"
B = "Part2"
C = A + "+" + B

print(C)

# Access like an array
A = "Hello World"
print(A[1])

# Looping through
A = "12345"
for X in A:
    print(X)

# Length
A = "123456"
print(len(A))

# Check if sth is in the string with "in" or "not in"
A = "I am so bored!"
print("am" in A) # returns True
print("ma" in A) # returns False
print("bo" in A) # returns True

print("am" not in A) # returns False

# Slicing
A = "ABC DEF XYZ"
print(A[1:5]) # "BC D"

print(A[:5]) # "ABC D"

print(A[1:]) # "BC DEF XYZ"

print(A[-5:-1]) # "F XY"

# Modification
## Upper case
A = "abc"
print(A.upper())

## Lower case
A = "ABC"
print(A.lower())

## Remove spaces beginning & End
A = "        Blub               "
print(A)
print(A.strip())

## Replace a part of a string
A = "ABC"
print(A.replace("B", "F")) # replace B with F

## Splitting
A = "ABC"
print(A.split("B"))

# F-Strings, placeholders and modifiers
A = 39
print(f"I am {A} years old")
print(f"I am {A:.2f} years old")
print(f"I am {30 + 9} years old")

# Escape characters
TXT = "We are the so-called \"Vikings\" from the north."
print(TXT)
# \'	Single Quote	
# \\	Backslash	
# \n	New Line	
# \r	Carriage Return	
# \t	Tab	
# \b	Backspace	
# \f	Form Feed	
# \ooo	Octal value	
# \xhh	Hex value

# String methods
# https://www.w3schools.com/python/python_strings_methods.asp
