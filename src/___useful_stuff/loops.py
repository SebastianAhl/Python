"Python loops"

print("\nPython loops")

# while loop
print("\nwhile loop")

I = 1
while I < 6:
    print("I:", I)
    I += 1
else: # else will not be executed if you use a break
    print("Finished")

print("Better then else")


# for loop
print("\nfor loop")

Devices = ["dev1", "dev2", "dev3"]
for X in Devices:
    print("Loop collection:", X)

print("\n")

for X in Devices[0]:
    print("Loop string:", X)


# for with range() function
print("\nfor with range() function")
print("Range 0..5")
for X in range(6): # 0..5
    print("Range:", X)

print("\nRange 2..5")
for X in range(2, 6): # 2..5
    print("Range:", X)

print("\nRange 2..20 step==5")
for X in range(2, 20, 5): # 2 ->7 -> 12 -> 17
    print("Range:", X)


# for with pass statement
print("\nfor with pass statement")
# if, for some reasons your for loop should be empty
for X in range(2, 6):
    pass


# break statement
# used to interrupt a loop

while 1:
    break


# continue statement
# jumps to the next iteration
while 1:
    if I == 1:
        continue
    break
