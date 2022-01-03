"""
Find the negative numbers in a list and print the list with only negative numbers.
"""

input_number = [ 1, 2, 3, -8, -9]
negative_numbers_list = []
for num in input_number:
    if num < 0:
        negative_numbers_list.append(num)

print(negative_numbers_list)
