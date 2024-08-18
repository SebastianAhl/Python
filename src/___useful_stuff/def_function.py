"Defining functions"

# global variables
X = "UB"
Y = "Access not granted"


# Definition section
# basic functions
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


# functions with parameters
# parameters are variables
# arguments are values of the variables
def func_1_parameter(name = "MyName"):
    "Function with one parameter and default value"
    print("Name:", name)

def func_2_parameter(name1, name2):
    "Function with two parameter and return value"
    print("name1:", name1, "name2:", name2)
    return "PASSED"

def func_only_positional_args(name1, name2, /):
    "Function with only positional arguments before ', /'. keys are not allowed"
    print("name1:", name1, "name2:", name2)

def func_only_key_args(*, name1, name2):
    "Function with only key arguments after '*,'"
    print("name1:", name1, "name2:", name2)

def func_combi_positional_key_args(name1, /, *, name2):
    "Function with a combination of positional and non positional arguments"
    print("name1:", name1, "name2:", name2)


# unknown amount of arguments: *key --> tuple
def func_tuple_argument(*names):
    "Function with one parameter (tuple) --> unknown arguments"
    print("Names:", names)


# several parameters with arguments: **key --> dictionary
def func_dict_argument(**names):
    "Function with one parameter (dictionary)"
    print("Names:", names["second"])


############################
############################
# Execution section
# basic functions
func_1()
print("X:", X)

global_var_redefined()
print("X:", X)

update_global()
print("Updated X:", X)

func_only_positional_args("NonPosName1", "NonPosName2")
# func_only_positional_args(name1= "NonPosName1", name2="NonPosName2") # doesn'work because of ', /'

# func_only_key_args("KeyName1", "KeyName2") # doesn'work because of '*,'
func_only_key_args(name1= "KeyName1", name2="KeyName2")

print("\n\n")
# functions with parameters
func_1_parameter("ABCDEF")
func_1_parameter()
RET = func_2_parameter("Name1", "Name2")
print("return value:", RET)


print("\n")
# using keywords
func_2_parameter(name2= "blu", name1= "bla")


print("\n")
# using tuple
func_tuple_argument("Name1", "Name2", "Name3", "Name4", "Name5")


print("\n")
# using dictionary
func_dict_argument(firt = "abc", second = "def")
