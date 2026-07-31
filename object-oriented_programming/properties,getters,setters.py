class Student:
    def __init__(self,id,name):
        self.id = id 
        self.name = name
        
    @property
    def id(self):
        print("id getter called")
        return self._id
    
    @id.setter
    def id(self,id):
        print("id setter called")
        self._id = id
        
    @property
    def name(self):
        print("name getter called")
        return self._name
    
    @name.setter
    def name(self,name):
        print("name setter called")
        if not name:
            raise ValueError("Name can't be empty.")
        self._name = name
            
    def __str__(self):
        return (f"Student ID: {self.id},Name: {self.name}")
        
def main():
    student = get_student()
    print(student)
    
def get_student():
        id = input("Enter your student id: ")
        name =  input("Enter your student name: ")
        return Student(2,"abdul jabbar")
    
if __name__ == "__main__":
    main()