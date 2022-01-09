nums = [1, 2, 3, 1, 1, 4]


def my_function(x):
    return list(dict.fromkeys(x))


mylist = my_function(nums)

print(mylist)

