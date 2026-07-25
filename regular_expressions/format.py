name = input("What's your name? ").strip()

if "," in name:
    first,last = name.split(", ")
    name = f"{first} {last}"
print(f"hello,{name}")

'''There are many bugs which we work on for this program.See "user_name_format.py"'''