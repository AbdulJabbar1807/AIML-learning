import re

email = input("Enter your email address: ")
if re.search(r"^[a-zA-Z0-9_]+@[a-z]+\.com$",email):
    print("Valid email address.")
else:
    print("Invalid email address.")