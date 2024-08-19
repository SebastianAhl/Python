"Iterators __iter__() __next__()"
# more information: https://www.w3schools.com/python/python_iterators.asp

# Iteration is the process of repeating a process to generate
# a sequence of outcomes123. # Each repetition of the process
# is called an iteration, # and the results of one iteration
# are used as the starting point for the next iteration.

print("\nIterators __iter__() __next__()")

MyTuple = ("ABC", 123, "DEF", 456)
MyIter = iter(MyTuple)

print("\nIteration of a Tuple:")
print(next(MyIter))
print(next(MyIter))
print(next(MyIter))
print(next(MyIter))
# print(next(MyIter)) # causes error because no element

MyString = "abcdef"
MyIter = iter(MyString)

print("\nIteration of a String:")
print(next(MyIter))
print(next(MyIter))
print(next(MyIter))
print(next(MyIter))
print(next(MyIter))
print(next(MyIter))
