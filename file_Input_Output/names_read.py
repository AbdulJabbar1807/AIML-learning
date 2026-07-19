names = input("Enter your name: ")

with open("names_read.txt","a") as file:
    file.write(f"{names}\n")
    
with open("names_read.txt") as file:
    lines = file.readlines()
    
for line in lines:
    print(f"hello,{line}".rstrip())