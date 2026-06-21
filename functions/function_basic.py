# greeting user
def greet(name):
    return (f"Assalam alaikum {name}")

name = input("Enter your name : ")
print(greet(name))

#Square number
def square_num(a):
    return a * a
a = int(input("Enter the value for a : "))
print(f"Square of the number a is {square_num(a)}")

# Odd or Even
def is_even(num):
    if num % 2 == 0:
        return("number is an Even number.")
    else:
        return("number is a Odd number.")
    
num = int(input("Enter the number : "))
print(is_even(num))
        

# To check if a user can drive or not
def can_drive(age):
    if age < 18:
        return ("you're under age,can't drive!")
    elif age >70:
        return ("you can drive,make sure to drive carefully.")
    else:
        return ("you can drive.")
    

age = int(input("Enter your age : "))
print(can_drive(age))