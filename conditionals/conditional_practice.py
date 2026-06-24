#Q1. User's age-
age = int(input("What's your age: "))

if age < 0:
    print("Invalid input!")
elif age <= 12:
    print("Child")
elif age <= 19:
    print("Teenager")
elif age <= 60:
    print("Adult")
else:
    print("Senior")