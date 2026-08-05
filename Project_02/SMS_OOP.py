class Studentmanagement:
    students = []
    def __init__(self) -> None:
        ...

class Student:
    def __init__(self,id,name,email) -> None:
        self.id = id
        self.name = name
        self.email = email
        
    def __str__(self) -> str:
        return f"ID: {self.id},Name: {self.name} and Email: {self.email}"
    
student1 = Studentmanagement.students.append(Student(1,"abdul","abdul@gmail.com"))
student2 = Studentmanagement.students.append(Student(2,"Ali","ali@gmail.com"))

print(Studentmanagement.students[0])
print(Studentmanagement.students[1])

