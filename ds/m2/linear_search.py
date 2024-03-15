# Linear search program to search an element
# return the index position of the #array

def linear_search(nums, el):
    for index, value in enumerate(nums):
        if value == el:
            return index

    return -1


arr = [3, 4, 1, 6, 14]
element = 4
print("Index position for the element x is:", linear_search(arr, element))
