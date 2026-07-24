import re
email = input("What's your email address: ")

if re.search(r"^\w+@(\w+\.)?\w+\.(com|edu|gov|org|in)$",email,re.DOTALL):
    print("Valid email address.")
else:
    print("Invalid email address.")
    