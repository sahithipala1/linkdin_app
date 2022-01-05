"""
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

"""

input_num = 121
temp = input_num
reverse = 0

while input_num > 0:
    reminder = input_num % 10
    reverse = reverse * 10 + reminder
    input_num = input_num // 10
if temp == reverse:
    print("it palindrome")
