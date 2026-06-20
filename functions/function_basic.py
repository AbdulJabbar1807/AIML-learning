# To check if a user can drive or not
def CanDrive(age):
    if age < 18:
        return ("you're under age,can't drive!")
    elif age >70:
        return ("you can drive,make sure to drive carefully.")
    else:
        return ("you can drive.")
    

age = int(input("Enter your age : "))
print(CanDrive(age))