list_of_num = [1, 1, 2, 3, 9]

min_num = list_of_num[0]

for temp_num in list_of_num[1:]:
    if temp_num != min_num:
        min_num = temp_num

print(min_num)
