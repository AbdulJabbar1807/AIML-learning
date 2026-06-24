# Comparison Operators and Conditional Operators.
x = int(input("What's x? "))
y = int(input("What's y? "))

if x > y:
    print("x is greater than y.")
elif x < y:
    print("x is less than y.")
else:
    print("x is equal to y.")
    
# Logical Operators - or,and,not equal.

if x > y or x < y: # or
    print("x is not equal to y.")
else:
    print("x is equal to y.")
    
if x != y: # not equal
    print("x is not equal to y.")
else:
    print("x is equal to y.")
    
'''Grade of students (Assuming out of 100)'''
score = int(input("Enter your score between 0 and 100: "))

if score >= 90:
    print("Grade: A")
elif score >=80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
elif score >= 50:
    print("Grade: E")
else:
    print("Grade: F")
    