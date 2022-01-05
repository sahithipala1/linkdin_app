x = 121
temp = x
rev = 0
while (x > 0):
    dig = x % 10
    rev = rev * 10 + dig
    x = x // 10
    if (temp == rev):
        print("The number is a palindrome!")
    else:
        print("The number isn't a palindrome!")
