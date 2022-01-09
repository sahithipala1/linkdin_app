symbol = ("( )", "{ }", "[ ]")
temporary = ("( )", "{ }", "[ ]")

for temporary in symbol:
    if temporary == symbol:
        print(True)
    else:
        print("not matching")
print(symbol[0])
print(symbol[0:2])
print(symbol[:])





