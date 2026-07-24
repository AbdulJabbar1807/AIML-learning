import re

email = input("Enter your email address: ")

if re.search(r"^[^@]+@[^@]+\.com$",email):
    print("Valid,email addess.")
else:
    print("Invalid,email address.")
