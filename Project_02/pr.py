class Student:
    def __init__(self,id,name,email):
        self.id = id
        self.name = name
        self.email = email
        
    def __str__(self) -> str:
        return f"id {self.id},name {self.name},email {self.email}"    
        
id = input("enter id: ")
name = input("enter name: ")
email = input("enter email address: ")

student = Student(id,name,email)

print(student.id)

