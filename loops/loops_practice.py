def main():
    number = get_number()
    hello(number)
    
    students = ["Abdul","Mohammed","Ali"]
    student(students)
    
    star = get_number()
    print_star(star)
    
    square = get_number()
    square_pattern(square)
    
    greeting = get_number()
    greet(greeting)
    
    count = get_number()
    count_down(count)
    
    positive_integer(number)
    
    print(iseven_number())
    
    print(password())
    
    print(marks())
    
    num = int(input("Enter the number for multiplication number: "))
    table(num)
    
    print(sum_of_num(number))
    
    print(factorial(number))
    
    # print(average(number))
    
#Q1. Validating user input    
def get_number():
    
    while True:
        n = int(input("What's n? "))
        if n>0:
            return n

def hello(i):
    for _ in range(i):
        print("hello")
        
#Q2. Iterating over a list of strings
def student(students):
    for student in range(len(students)):
        print(student)

#Q3. Print star
def print_star(star):
    for _ in range(star):
        print("*",end="")
    print()
        
#Q4. Square pattern-
def square_pattern(square):
    for _ in range(square):
        for j in range(square):
            print("*",end="")
        print()

#Q5. Greetings
def greet(n):
    for _ in range(n):
        print("Hello,Abdul")
        
#Q6. Countdown
def count_down(n):
    for i in range(n):
        print(n-i)
    print("Blast Off")

#Q7. Positive interger
def positive_integer(n):
    return n

#Q8. Even number validation
def iseven_number(even_num = ""):
    while True:
        even_num = int(input("What's the number: "))
        if even_num % 2 == 0:
            return even_num
        
#Q9. Password
def password(word=""):
    while True:
        word = input("Enter your password: ")
        if word == "python123":
            return "Access granted"
        
#Q10. Marks between 0 and 100
def marks(m=""):
    while True:
        m = int(input("What's your marks? "))
        if 0 <= m <= 100:
            return m
        
#Q11. Multiplication table
def table(num):
    for i in range(1,11):
        print(f"{num} x {i} = {num*i}")
        
#Q12. Sum of n numbers using loops
def sum_of_num(number):
    total = 0
    for i in range(1,number+1):
        total += i
    return total

#Q13. Factorial number
def factorial(factorial):
    fact = 1
    for i in range(1,factorial+1):
        fact *= i
    return fact


        
main()


