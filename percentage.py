print(121 % 10)
print(121 // 10)
print(0 * 10 + 121 / 10)

input_number = 121
reverse_of_number = 0
while input_number > 0:
    dig = input_number % 10
    reverse_of_number = reverse_of_number * 10 + dig
    input_number = input_number // 10
if input_number == reverse_of_number:
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")
