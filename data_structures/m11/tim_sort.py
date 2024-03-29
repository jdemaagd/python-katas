# NOTE: python's timsort combines insertion into its algorithm
def insertion_sort(unsorted_list):
    for index in range(1, len(unsorted_list)):
        search_index = index
        insert_value = unsorted_list[index]
        while search_index > 0 and unsorted_list[search_index - 1] > insert_value:
            unsorted_list[search_index] = unsorted_list[search_index - 1]
            search_index -= 1
        unsorted_list[search_index] = insert_value
    return unsorted_list


# NOTE: python's timsort combines merge into its algorithm
def merge(first_sublist, second_sublist):
    i = j = 0
    merged_list = []
    while i < len(first_sublist) and j < len(second_sublist):
        if first_sublist[i] < second_sublist[j]:
            merged_list.append(first_sublist[i])
            i += 1
        else:
            merged_list.append(second_sublist[j])
            j += 1
    while i < len(first_sublist):
        merged_list.append(first_sublist[i])
        i += 1
    while j < len(second_sublist):
        merged_list.append(second_sublist[j])
        j += 1
    return merged_list


def tim_sort(arr, run):
    for x in range(0, len(arr), run):
        arr[x: x + run] = insertion_sort(arr[x: x + run])
    runSize = run

    while runSize < len(arr):
        for x in range(0, len(arr), 2 * runSize):
            arr[x: x + 2 * runSize] = merge(arr[x: x + runSize], arr[x + runSize: x + 2 * runSize])

        runSize = runSize * 2


arr1 = [4, 6, 3, 9, 2, 8, 7, 5]
run1 = 2

tim_sort(arr1, run1)
print(arr1)
