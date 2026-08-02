class Student:
    def __init__(self,name,id) -> None:
        self.name = name
        self.id = id
        
    def __str__(self):
        return (f"Student name is {self.name},Id {self.id}")
        
    @classmethod
    def get(cls):
        name = input("Enter your name: ")
        id = input("Enter your id: ")
        return cls(name,id)
    
def main():
    student = Student.get()
    print(student)
    
if __name__ == "__main__":
    main()
