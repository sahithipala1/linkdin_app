def brackets(expression):
    given_symbols = ['()', '{}', '[]']
    while any(x in expression for x in given_symbols):
        for y in given_symbols:
            expression = expression.replace(y, '')
    return not expression


# calling the function
input_string = "[]{}()"
if brackets(input_string):
    print(input_string, "balanced")
else:
    print(input_string, "Not balanced")