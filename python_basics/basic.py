print("hello world")

# Ask user there name
name = input("Enter your name ") # '=' here is assignment operator , it copies the return valur of right to left.
# Greet user 
print(f"hello,{name}")
print("hello,",name)

print("hello ", name, sep='???')
print("hello",end='')
print(name)


# Dictionaries in python.
students = [
    {"name":"Abdul","branch":"CSE","year":"1st"},
    {"name":"Mohammed","branch":"AIML","year":"2nd"},
    {"name":"Ali","branch":"CY","year":"3rd"},
]
for student in students:
    print(student["name"],student["branch"],student["year"])


    



    

