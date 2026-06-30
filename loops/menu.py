def main():
    menu()

def menu():
    while True:
        display_menu() 
        choice = user_choice()
        
        match choice:
            case 1:
                side = get_number()
                square_pattern(side)
                
            case 2:
                print(password())     
                
            case 3:
                num = get_number()
                result = factorial(num)
                print(result)
         
            case 4:
                print(calculate_average())
                
            case 5:
                number = get_number()
                print(sum_of_num(number))
                
            case 6:
                score = marks()
                print(f"Valid marks: {score}")
                
            case 7:
                num = get_number()
                table(num)
                
            case 8:
                print(iseven_number(),"is an even number.")
                
            case 9:
                count = get_number()
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
    return int(input("Enter your choice: "))

# Valid input
def get_number():
    while True:
        n = int(input("What's the number: "))
        if n > 0:
            return n
        else:
            print("Invalid input try again!")

# Square pattern-
def square_pattern(side):
    for _ in range(side):
        for j in range(side):
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
    n = int(input("enter the 'n': "))
    item_list = []
    
    for i in range(n):
        num = int(input("enter the number: "))
        item_list.append(num)

    total_sum = 0
    for j in item_list:
        total_sum += j
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
        m = int(input("What's your marks? "))
        if 0 <= m <= 100:
            return m
        else:
            print("Invalid marks please try again!")
            
# Multiplication table
def table(num):
    for i in range(1,11):
        print(f"{num} x {i} = {num*i}")
        
# Even number validation
def iseven_number():
    while True:
        even_num = int(input("What's the number: "))
        if even_num % 2 == 0:
            return even_num
        else:
            print("Invalid try again!")
            
# Countdown
def count_down(n):
    for i in range(n):
        print(n-i)
    print("Blast Off")

main()