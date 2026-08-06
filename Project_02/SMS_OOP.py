import sys

class StudentManagement():
    def __init__(self) -> None:
        self.students = []
        
    def add_student(self,id,name,email):
        student = Student(id,name,email)
        self.students.append(student)
        
    def view_student(self):
        for student in self.students:
            print(student)
    
class Student:
    def __init__(self,id,name,email) -> None:
        self.id = id
        self.name = name
        self.email = email
        
    def __str__(self) -> str:
        return f"ID: {self.id},Name: {self.name} and Email: {self.email}"

def main():
    sms = StudentManagement()
    menu(sms)

def menu(sms):
    while True:
        display_menu()
        choice = int(input("Enter your choice: "))
        match choice:
            case 1:
                id = int(input("Enter your student id: "))
                name = input("What's your name: ")
                email = input("Enter your email address: ")
                sms.add_student(id,name,email)
            case 2:
                sms.view_student()
            case 3:
                print("Thankyou for using SMS.")
                sys.exit()
            case _:
                print("Please enter only positive integer only.")

def display_menu():
        print("Main Menu-")
        print("1.Add Students.")
        print("2.View Students.")
        print("3.Exit.")               

if __name__ == "__main__":
    main()



