# using 'in' operator
mylist1 = [100, 20, 30, 40]
mylist2 = [10, 50, 60, 90]
if mylist1[1] in mylist2:
    print("elements are overlapping")
else:
    print("elements are not overlapping")

# Output:
# elements are not overlapping

val = 104
mylist = [100, 210, 430, 840, 108]
if val not in mylist:
    print("val is NOT present in mylist")
else:
    print("val is  present in mylist")

# Output:
# val is NOT present in mylist

list1 = []
list2 = []
if list1 == list2:
    print("Both are equal")
else:
    print("Both are not equal")
if list1 is list2:
    print("Both variables are pointing to the same object")
else:
    print("Both variables are not pointing to the same object")
thirdList = list1
if thirdList is list2:
    print("Both are pointing to the same object")
else:
    print("Both are not pointing to the same object")
'''
Output:
Both are equal	
Both variables are not pointing to the same object
Both are pointing to the same object
'''

list3 = []
list4 = []
if list3 is not list4:
    print("Both list3 and list4 variables are the same object")
else:
    print("Both list3 and list4 variables are not the same object")

# Output:
# Both list3 and list4 variables are the same object
