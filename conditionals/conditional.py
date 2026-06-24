# Conditionals,if-elif-else.
x = int(input("What's x? "))
y = int(input("What's y? "))

if x > y:
    print("x is greater than y.")
elif x < y:
    print("x is less than y.")
else:
    print("x is equal to y.")
    
# or,and,not equal.

if x > y or x < y: # or
    print("x is not equal to y.")
else:
    print("x is equal to y.")
    
if x!=y: # not equal
    print("x is not equal to y.")
else:
    print("x is equal to y.")
    
'''Grade of students (Assuming out of 100)'''
score = int(input("Enter your score between 0 and 100: "))

if 90 <= score:
    print("Grade: A")
elif 80 <= score:
    print("Grade: B")
elif 70 <= score:
    print("Grade: C")
elif 60 <= score:
    print("Grade: D")
elif 50 <= score:
    print("Grade: E")
else:
    print("Grade: F")
    