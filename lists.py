# print the smallest number in the given  list.

list_of_num = [9, 5, 10, 2]

min_num = list_of_num[0]

for temp_num in list_of_num[1:]:
    if temp_num < min_num:
        min_num = temp_num

print(min_num)

input_nums = [1, 2, 3, -9]

for numbers in input_nums:
    if numbers < 0:
        print(numbers)

given_nums = [1, 2, 3, -9, 1, 2, 3, -8]

for num in given_nums:
    if num < 0:
        print(num)

