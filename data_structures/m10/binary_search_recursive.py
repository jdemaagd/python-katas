def binary_search_recursive(ordered_list, first, last, term):
    # NOTE: we've crossed midpoint, so have not found the term
    if last < first:
        return None
    else:
        mid = first + ((last - first) // 2)

        if ordered_list[mid] > term:
            return binary_search_recursive(ordered_list, first, mid - 1, term)
        elif ordered_list[mid] < term:
            return binary_search_recursive(ordered_list, mid + 1, last, term)
        else:
            return mid


list1 = [10, 30, 100, 120, 500]

search_term = 10
index_position1 = binary_search_recursive(list1, 0, len(list1) - 1, search_term)
if index_position1 is None:
    print("The data item {} is not found".format(search_term))
else:
    print("The data item {} is found at position {}".format(search_term, index_position1))

list2 = ['book', 'data', 'packt', 'structure']

search_term2 = 'data'
index_position2 = binary_search_recursive(list2, 0, len(list1) - 1, search_term2)
if index_position2 is None:
    print("The data item {} is not found".format(search_term2))
else:
    print("The data item {} is found at position {}".format(search_term2, index_position2))
