########## Program to illustrate 'not in' operator
val = 104
mylist = [100, 210, 430, 840, 108]
if val not in mylist:
    print("val is NOT present in mylist")
else:
    print("val is  present in mylist")

# Output:
# val is NOT present in mylist


############# Example program to demonstrate the use of 'is' operator
Firstlist = []
Secondlist = []
if Firstlist == Secondlist:
    print("Both are equal")
else:
    print("Both are not equal")
if Firstlist is Secondlist:
    print("Both variables are pointing to the same object")
else:
    print("Both variables are not pointing to the same object")
thirdList = Firstlist
if thirdList is Secondlist:
    print("Both are pointing to the same object")
else:
    print("Both are not pointing to the same object")
'''
Output:
Both are equal	
Both variables are not pointing to the same object
Both are pointing to the same object
'''

####### Example program to demonstrate the use of 'is not' operator
Firstlist = []
Secondlist = []
if Firstlist is not Secondlist:
    print("Both Firstlist and Secondlist variables are the same object")
else:
    print("Both Firstlist and Secondlist variables are not the same object")

# Output:
# Both Firstlist and Secondlist variables are the same object

