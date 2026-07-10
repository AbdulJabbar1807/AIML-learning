def main():
    menu()

def menu():
    all_student = []
    while True:
        display_choice()
        choice = user_choice()
        match choice:
            case 1:
                add_student(all_student)
                
            case 2:
                view = all_student
                view_student(view)
            
            case 3:
                print("Thankyou.")
                break
            
            case _:
                print("Please enter a valid input.")
    
def display_choice():
    print("Choose the choice.")
    print("1.Add Student's.")
    print("2.View Student's.")
    print("3.Exit.")
    
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
            
def add_student(student):
    stu_id = input("Enter your student ID: ")
    student.append({"ID":stu_id})
    student[0]["name"] = input("Enter student name: ")

def view_student(view):
    print("-"*50)
    print("Student's name.")
    for v in view:
        print(f"Id: {v["ID"]},Name: {v["name"]}")
        
    
menu()
