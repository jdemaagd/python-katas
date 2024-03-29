a = 32
b = 132
if a > 0 and b > 0:
    print("Both a and b are greater than zero")
else:
    print("At least one variable is less than 0")

# Output:
# Both a and b are greater than zero

a = 32
b = -32
if a > 0 or b > 0:
    print("At least one variable is greater than zero")
else:
    print("Both variables are less than 0")

# Output:
# At least one variable is greater than zero

a = 32
if not a:
    print("Boolean value of a is False")
else:
    print("Boolean value of a is True")

# Output:
# Boolean value of a is True

tupleName = ("entry1", "entry2", "entry3")
myTuple = ("Shyam", 23, True, "male")
print(len((4, 5, 'hello')))

print((4, 5) + (10, 20))
print((2, 1) * 3)
print(3 in ('hi', 'xyz', 3))
for p in (6, 7, 8):
    print(p)

x = ('hello', 'world', 'india')
print(x[1])
print(x[-2])
print(x[1:])
