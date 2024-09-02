# Sources
## w3schools
Python course: https://www.w3schools.com/python/
- Nicely structured
- Easy to follow
- For beginners as well as experienced developers
- Progress can be saved with a free account
- Offers paid exams


# Terms and definitions
## Modules
[Source Modules](https://www.w3schools.com/python/python_modules.asp)

> [!NOTE]
> A module is a kind of library in another '.py' file.

- Create a '.py' file --> module
- Define/ Declare whatever you want in the new module (`def <...>`, variables of all types)
- Import the module with the keyword `import <modulename>` and only the modulename without '.py'
- You can rename a module when importing it with the keyword `as`. `import <modulename> as <new name>`
- You can import parts you need from a module. `from <modulename> import <moduel part>`


## Polymorphism
[Source Polymorphism](https://www.w3schools.com/python/python_polymorphism.asp)

> [!NOTE]
> The word "polymorphism" means "many forms", and in programming it refers to 
> methods/functions/operators with the same name that can be executed on many 
> objects or classes.

For example if three classes and three objects (car1, boat1, plane1) have a method with the same name, we can use it in a loop:
```
for x in (car1, boat1, plane1):
  x.move()
```


## Scope
[Source Scope](https://www.w3schools.com/python/python_scope.asp)

> [!NOTE]
> The scope defines where a variable can be accessed.

The keyword `global`can access global variables:
```
x = 300

def myfunc():
  global x
  x = 200

myfunc()

print(x)
```

The keyword `nonlocal`makes variables available to outside functions:
```
def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())
```

# PIP - Python Package Manager
[Source PIP](https://www.w3schools.com/python/python_pip.asp)

## Check installation
`pip --version`

## List installed packages
`pip list`

## (Un)Install package
`pip install <PACKAGENAME>`
`pip uninstall <PACKAGENAME>`

## Package Repository
[Source PIP Repo](https://pypi.org/)
