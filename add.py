nums = [2, 7, 11, 15]
target = 26

# Brute force solution
for outer_index in range(len(nums)):
    for inner_index in range(outer_index+1, len(nums)):
        if nums[outer_index] + nums[inner_index] == target:
            print(outer_index, inner_index)

""" while loop"""
print("while loop")

# While loop solution
for outer_index in range(len(nums)):
    inner_index = outer_index + 1
    while inner_index < len(nums):
        print(outer_index, inner_index)
        if nums[outer_index] + nums[inner_index] == target:
            print("Answer", outer_index, inner_index)

        inner_index = inner_index + 1
