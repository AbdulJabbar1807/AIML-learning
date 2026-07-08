# print(f"x is {x}") # on providing a literal -> 'CA' it will give a value error.

try:
    x = int(input("What's "))
except ValueError:
    print("x is invalid interger.")
else:
    print(f"x is {x}") # will give a 'NameError' if an exception is there and no else is used.