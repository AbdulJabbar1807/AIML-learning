def main():
    menu()

def menu():
    while True:
        display_choice()
        choice = user_choice()
        match choice:
            case 1:
                number_of_student = get_number()
                add_student(number_of_student)
            
            case 2:
                print("Thankyou.")
                break
            
            case _:
                print("Please enter a valid input.")
    
def display_choice():
    print("1.Add Student.")
    print("1.Exit.")
    
def user_choice():
    while True:
        try:
            return int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid choice.")
            
def get_number():
    while True:
        try:
            n = int(input("Enter a positive number: "))
            if n > 0:
                return n
            print("Enter a number greater than zero.")
        except ValueError:
            print("Please enter a valid input.")
            
def add_student(total_student):
    student = []
    
menu()
