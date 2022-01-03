m = [1, 2, 3, 1]

# Initial assumption
found_duplicate = False

# Processing
for i in range(len(m)):
    for inner_index in range(i + 1, len(m)):
        if m[i] == m[inner_index]:
            found_duplicate = True

# Final answer
print(found_duplicate)


for i in range(5):
    print(i * i)
