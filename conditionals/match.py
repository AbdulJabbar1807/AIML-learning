name = input("What's the name? ")

#Method 1
# if name == "Abdul Jabbar":
#     print("Saudi Arabia")
# elif name == "Abdul Rehman":
#     print("Saudi Arabia")
# elif name == "Abdul Sattar":
#     print("Saudi Arabia")
# elif name == "David":
#     print("Britain")
# elif name == "John":
#     print("Britain")
# else:
#     print("Who?")

#Method 2
match name.title():
    case "Abdul Jabbar" | "Abdul Sattar" | "Abdul Rehman":
        print("Saudi Arabia")

    case "David" | "John":
        print("Britain")

    case _:
        print("Who?")
    
    