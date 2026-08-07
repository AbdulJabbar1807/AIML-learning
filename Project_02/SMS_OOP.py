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
    
    def search_student(self,search):
        for student in self.students:
            if student.id == search:
                return ({student.id},{student.name},{student.email})
        else:
            return "Student is not in the list."
        
    def delete_student(self,delete):
        for student in self.students:
            if student.id == delete:
                self.students[:] = [student for student in self.students if student.id != delete]
                return "Student successfully removed from the list."
        else:
            return "Student is not in the list."
        
    def update_student(self,update,id,name,email):
        for student in self.students:
            if student.id == update:
                student.update(id,name,email)
                return "Student successfully updated."
        else:
            return "Student is not in the list."
    
class Student:
    def __init__(self,id,name,email) -> None:
        self.id = id
        self.name = name
        self.email = email
        
    def __str__(self) -> str:
        return f"ID: {self.id},Name: {self.name} and Email: {self.email}"
    
    def update(self,new_id,new_name,new_email):
        self.id = new_id
        self.name = new_name
        self.email = new_email

def main():
    sms = StudentManagement()
    menu(sms)

def menu(sms):
    while True:
        display_menu()
        choice = get_number("Enter your choice: ")
        match choice:
            case 1:
                id = get_number("Enter your student id: ")
                name = input("What's your name: ")
                email = input("Enter your email address: ")
                sms.add_student(id,name,email)
            case 2:
                sms.view_student()
                
            case 3:
                search = get_number("Enter student ID to search in SMS: ")
                id,name,email = sms.search_student(search)
                print(f"Student detail-\nID: {id}\nName: {name}\nEmail: {email}")
                
            case 4:
                delete = get_number("Enter student ID to delete from SMS: ")
                print(sms.delete_student(delete))
                
            case 5:
                update = get_number("Enter student ID detail to update Student in SMS: ")
                id,name,email = update_details()
                print(sms.update_student(update,id,name,email))            
            case 6:
                print("Thankyou for using SMS.")
                sys.exit()
            case _:
                print("Please enter only positive integer only.") 
                
def display_menu():
    print("Main Menu-")
    print("1.Add Students.")
    print("2.View Students.")
    print("3.Search Students.")
    print("4.Delete Student.")
    print("5.Update Student.")
    print("6.Exit.")
        
def get_number(prompt):
    while True:
        try:
            n = int(input(prompt))
            if n > 0:
                return n
        except ValueError:
            print("Enter only positive integer.")
            
def update_details():
    new_id = get_number("Enter your new id: ")
    new_name = input("Enter your new name: ")
    new_email = input("Enter your new email: ")
    return new_id,new_name,new_email

if __name__ == "__main__":
    main()



