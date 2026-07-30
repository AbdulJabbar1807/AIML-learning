class Student:
    def __init__(self,id,name,email):
        if not name:
            raise ValueError("Please enter a valid name!")
        if not email:
            raise email("Please enter a valid email address!")
        self.id = id
        self.name = name
        self.email = email
        
    def __str__(self):
        return (f"Student ID: {self.id},Name: {self.name} and Email: {self.email}")
        
def main():
    student = get_student()
    print(student)
    
def get_student():
        id = input("Enter your student id: ")
        name =  input("Enter your student name: ")
        email = input("Enter your student email: ")
        return Student(id,name,email)
    
if __name__ == "__main__":
    main()