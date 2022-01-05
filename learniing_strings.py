symbol = ("( )", "{ }", "[ ]")
temporary = ("( )", "{ ", "[ ]")

for temporary in symbol:
    if temporary == symbol:
        print(True)
    else:
        print("not matching")
print(symbol[0])
print(symbol[0:2])
print(symbol[:])

nums = ("( )", "[ ]", "{ }")
target = "( )"
for outer_index in range(len(nums)):
    for inner_index in range(outer_index + 1, len(nums)):
        if nums[outer_index] + nums[inner_index] == target:
            print(outer_index, inner_index)
