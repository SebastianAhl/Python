"JSON for storing and exchanging data"
# more information: https://www.w3schools.com/python/python_json.asp

# module built into python
import json

# example JSON string:
X = '{ "brand":"apple", "model":"iphone", "version":15}'

# convert/ parse from json string to python dict
print("\nconvert/ parse from json string to python dict")
print("Version:", json.loads(X)["version"])

# convert/ parse from python dict to json string
print("\nconvert/ parse from python dict to json string")

# example python dict
Y = {
    "brand":"apple", 
    "model":"iphone", 
    "version":15
    }

print("JSON String:", json.dumps(Y))

# examples how to convert python objects into json strings
print("\nexamples how to convert python objects into json strings")
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))
