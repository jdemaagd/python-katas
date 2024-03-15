def squares(n):
    square_numbers = []
    for number in n:
        square_numbers.append(number * number)
    return square_numbers


nums = [2, 3, 5, 8]
print(squares(nums))
