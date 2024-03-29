def insertion_sort(nums):
    for index in range(1, len(nums)):
        search_index = index
        insert_value = nums[index]

        while search_index > 0 and nums[search_index - 1] > insert_value:
            nums[search_index] = nums[search_index - 1]
            search_index -= 1

        nums[search_index] = insert_value


my_list = [5, 1, 100, 2, 10]
print("Original ist", my_list)
insertion_sort(my_list)
print("Sorted list", my_list)
