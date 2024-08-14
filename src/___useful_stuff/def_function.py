"Defining functions"
# global variable
X = "UB"
Y = "Access not granted"

def func_1():
    "function declaration"
    print("BL" + X)

def global_var_redefined():
    "something I think you shouldn't do: declare a local variable with the same name like global"
    X = "NONONO!!!!!"
    print("X:", X)

def update_global():
    "Access global variables, not the nice way"
    global Y
    Y = "Access granted"

# execute the functions
func_1()
print("X:", X)

global_var_redefined()
print("X:", X)

update_global()
print("Updated X:", X)
