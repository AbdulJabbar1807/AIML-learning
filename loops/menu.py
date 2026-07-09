def main():
    menu()

def menu():
    while True:
        display_menu() 
        choice = user_choice()
        
        match choice:
            case 1:
                side = get_number("Enter the side of square? ")
                square_pattern(side)
                
            case 2:
                print(password())     
                
            case 3:
                num = get_number("Enter a number for factorial: ")
                result = factorial(num)
                print(result)
         
            case 4:
                print(calculate_average())
                
            case 5:
                number = get_number("Enter 'N' number's: ")
                print(sum_of_num(number))
                
            case 6:
                score = marks()
                print(f"Valid marks: {score}")
                
            case 7:
                num = get_number("What's number for multiplication table? ")
                table(num)
                
            case 8:
                print(iseven_number(),"is an even number.")
                
            case 9:
                count = get_number("Enter number for count-down: ")
                count_down(count)
                
            case 10:
                print("Thankyou")
                break
                                 
            case _:
                print("Invalid choice,Please enter correct choice.")    

# Menu
def display_menu():
        print("Choose option-")
        print("1. Square pattern")
        print("2. Password verification")
        print("3. Factorial")
        print("4. Calculate average")
        print("5. Sum of 'N' numbers")
        print("6. Validating Mark's")
        print("7. Multiplication table")
        print("8. Even number validation")
        print("9. Count-Down")
        print("10. Exit")
        print("-" * 50)

# User's choice
def user_choice():
    while True:
        try:
            return int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid choice.")

# Valid input
def get_number(prompt):
    while True:
        try:
            n = int(input(prompt))
            if n > 0:
                return n
            print("Enter a number greater than zero.")
        except ValueError:
            print("Please enter a valid number.")

# Square pattern-
def square_pattern(side):
    for _ in range(side):
        for _ in range(side):
            print("*",end="")
        print()

# Password
def password():
    while True:
        word = input("Enter your password: ")
        if word == "python123":
            return "Access granted"
        else:
             print("Invalid password please try again.")
          
# Factorial number
def factorial(num):
    fact = 1
    for i in range(1,num+1):
        fact *= i
    return fact
    
# Calculate average of 'N' different number's.
def calculate_average():
    n = get_number("Enter value for 'N' digits: ")
    
    item_list = []
    
    for _ in range(n):
        num = get_number("enter the number: ")
        item_list.append(num)
        
    total_sum = 0
    for number in item_list:
        total_sum += number
    average = total_sum/n
    return average

# Sum of n numbers using loops
def sum_of_num(number):
    total = 0
    for i in range(1,number+1):
        total += i
    return total

# Mark's validation.
def marks():
    while True:
        mark = get_number("What's your marks? ")
        if 0 <= mark <= 100:
            return mark
        else:
            print("Invalid marks please try again!")
            
# Multiplication table
def table(num):
    for i in range(1,11):
        print(f"{num} x {i} = {num*i}")
        
# Even number validation
def iseven_number():
    while True:
        even_num = get_number("Enter a even number: ")
        if even_num % 2 == 0:
            return even_num
        else:
            print("Enter a valid even number.")
            
# Countdown
def count_down(n):
    for i in range(n):
        print(n-i)
    print("Blast Off")

main()