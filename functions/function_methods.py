# Taking user name with removing extra spaces and capitalising first letter of each word in full name.
name = input("Enter your Name : ").strip().title()
print(name)

first,last = name.split(' ')
print(f"Your first name is : {first}")
print(f"Your last name is : {last}")

print(name.upper())
print(name.lower())
print(name.count('a'))
print(name.find('J'))
print(name.format())
print(len(name))