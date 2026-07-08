while True:
    try:
        number = int(input("What's the number? "))
    except ValueError:
        print("number is not an integer.")
    else:
        break
print(f"Your entered number is {number}")