unordered_list = [5, 2]

temp = unordered_list[0]
unordered_list[0] = unordered_list[1]
unordered_list[1] = temp

print(unordered_list)


def bubble_sort(nums):
    curr_it = len(nums) - 1
    for i in range(curr_it, 0, -1):
        for j in range(i):
            if nums[j] > nums[j + 1]:
                tmp = nums[j]
                nums[j] = nums[j + 1]
                nums[j + 1] = tmp


my_list = [4, 3, 2, 1]
bubble_sort(my_list)
print(my_list)

my_list = [1, 12, 3, 4]
bubble_sort(my_list)
print(my_list)
