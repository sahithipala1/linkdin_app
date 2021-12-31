m = [1, 2, 3, 1]

for i in range(len(m)):
    for inner_index in range(i + 1, len(m)):
        if m[i] == m[inner_index]:
            print(True)
        else:
            print(False)

