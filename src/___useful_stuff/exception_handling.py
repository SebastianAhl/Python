"Examples for exception_handling"

# source: https://www.w3schools.com/python/python_try_except.asp

    # Block         Description
    # try           Tests a Block of code for errors
    # except        Exception handling
    # else          Code executed when there is no error
    # finally       Code that is always executed

# further information:
    # https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/bare-except.html
    # https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/broad-exception-caught.html

print("\n##### Exception Types #####")

try:
    print(Not_Defined)
except Exception:
    print("Except type: Exception")


try:
    print(Not_Defined)
except NameError:
    print("Except type: NameError")


try:
    import not_existing
except ImportError:
    print("Except type: ImportError")


# except ImportError will not run because it isn't an ImportError
try:
    print(Not_Defined)
except ImportError:
    print("Except type: ImportError")
except Exception:
    print("Unknown error")


#  Else if there is no error
print("\n##### Else #####")
try:
    print("There is no error, so this will be printed")
except Exception:
    print("There won't be an error")
else:
    print("There is really no error and so else is executed")


# Finally that will always be executed
print("\n##### Finally #####")
try:
    print("There is no error, so this will be printed")
except Exception:
    print("There won't be an error")
else:
    print("There is really no error but else is executed")
finally:
    print("The finally section is always executed")


# Raise your own exception
print("\n##### Raise Exceptions #####")

MY_NUM = 1

# if My_Num < 10:
#     raise Exception("Number too small")

# if type(MY_NUM) is not str:
#     raise TypeError("Not a String")

# no exception raised
if not isinstance(MY_NUM, int):
    raise TypeError("It is not an int")
else:
    print("It is an int")

# exception raised
if not isinstance(MY_NUM, str):
    raise TypeError("Not a String")
