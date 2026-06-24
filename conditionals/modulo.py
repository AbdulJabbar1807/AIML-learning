def main():
    number = int(input("What's the number: "))
    if is_even(number):
        print(f"{number} is Even")
    else:
        print(f"{number} is Odd")
        
    
def is_even(number):
    #Method 1
    # if number%2 == 0:
    #     return True
    # else:
    #     return False
    
    #Method 2
    # return True if number % 2 == 0 else False
    
    #Method
    return number % 2 == 0

main()

