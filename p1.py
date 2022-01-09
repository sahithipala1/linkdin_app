# Given list A
listA = ['A', 'B', 'B','X']

# Given list B
listB= ['B', 'X', 'Z', 'P']

# Creating the result set
res = list(listA)

# Extending result with list B
res.extend(i for i in listB if i not in res)

# Get result
print(res)