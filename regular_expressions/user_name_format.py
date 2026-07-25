import re
name = input("What's your name? ")
if matches := re.search(r"^(.+), *(.+)$",name):
    name = (f"{matches.group(1)} {matches.group(2)}")

print(f"hello {name}")