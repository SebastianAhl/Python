"Python object oriented programming - classes and objects"
# keyword class

# simple class
class Phone:
    "Class Phone"
    Version = 19


# __init__() class function --> always executed when class is initiated
# __str__() class function --> return value of a class

# self parameter:
    # reference to the current object and used to access variable of the class
    # name don't need to be self. it just needs to be the first parameter
class OtherPhone:
    "Other Phone"
    def __init__(self, model, version):
        self.model = model
        self.version = version

    def __str__(self):
        return f"{self.model}({self.version})"


# Object methods --> functions that belong to the class/object
class OtherPhone2:
    "Other Phone2"
    def __init__(self, model, version):
        self.model = model
        self.version = version

    def print_my_phone(self):
        "Description"
        print("This is my phone:", self.model,  self.version)


# inheritance
class NewerPhone(OtherPhone2):
    "Description"
    def __init__(self, model, version, os): # --> overrides parent __init__() if not next line
        OtherPhone2.__init__(self, model, version) # imports parent __init__()

        self.os = os # extend __init__() of child

class NewestPhone(OtherPhone2):
    "super() function" # inherits all the methods and properties of parent
    def __init__(self, model, version, os): # --> overrides parent __init__() if not next line
        super().__init__(model, version)

        self.os = os # extend __init__() of child
        self.year = 2015 # extra parameter

    def do_sth(self):
        "Description"
        print("abc")


############################
############################
# object creation
print("\n")

# simple object creation
print("basic object creation")
phone1 = Phone()
print("Version of Phone:", phone1.Version)


# __init__() __str__() class function
print("\n__init__() __str__() class function")
apple = OtherPhone("iphone", 13)
print("Model:", apple.model)
print("Version:", apple.version)

print("\nReturn value:", apple)


# class functions
print("\nclass functions")
samsung = OtherPhone2("z", 4)
samsung.print_my_phone()


# change values
samsung.model = "galaxy"
samsung.print_my_phone()


# delete objects
del phone1


# inheritance
print("\n")
sony = NewerPhone("experia", 14, "Android")
print("Model:", sony.model)
print("Version:", sony.version)
print("OS:", sony.os)
