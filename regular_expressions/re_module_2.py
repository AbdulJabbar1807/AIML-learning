import re
email = input("What's your email address: ")

if re.fullmatch(r"^\w+@(\w+\.)?\w+\.(com|edu|gov|org|in)$",email,re.IGNORECASE):
    print("Valid email address.")
else:
    print("Invalid email address.")
    