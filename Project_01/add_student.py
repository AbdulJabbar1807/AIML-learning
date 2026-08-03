class Student:
    def __init__(self,id,name,email) -> None:
        self.id = id
        self.name = name
        self.email = email
        
    def __str__(self) -> str:
        return f"Student ID {self.id},Name {self.name},Email {self.email}"
    
    @classmethod
    def get(cls):
        id = input("Enter your id: ")
        name = input("Enter your name: ")
        email = input("Enter your email address: ")
        return cls(id,name,email)
    
def main():
    all_students = []
    while True:
        choice = input("Add student (y/n): ").strip().lower()
        if choice == "y":
            add_student(all_students)
        else:
            break

    print("------All Enrolled students-------")
    for student in all_students:
        print(student)
    
def add_student(student_list):        
    student_list.append(Student.get())
    
if __name__ == "__main__":
    main()