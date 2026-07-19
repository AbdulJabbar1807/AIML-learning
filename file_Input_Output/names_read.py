with open("names_read.txt") as file:
    for line in file:
        print(f"hello,{line}".rstrip())
    
