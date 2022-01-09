m = ["{}", "{}", "[}", "[)"]

print(range(len(m)))

# Initial assumption


# Processing
for i in range(len(m)):
    for inner_index in range(i + 1, len(m)):
        if m[i] == m[inner_index]:
            print("its true")
        else:
            print("not true")

areas = ["bathroom", "hall", "bedroom"]

expression = areas.append("game_room")
print(expression)


# new

list_of_num = [1, 1, 2]

min_num = list_of_num[0]

for temp_num in list_of_num[1:]:
    if temp_num == min_num:
        min_num = temp_num

print(min_num)
