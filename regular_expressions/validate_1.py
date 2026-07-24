email = input("What's your email address: ")

username,domain = email.split('@')
if username and domain.endswith(".com"):
    print("Valid email address.")
else:
    print("Invalid email address.")