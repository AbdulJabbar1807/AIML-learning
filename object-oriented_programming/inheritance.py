class Name:
    def __init__(self,name):
        if not name:
            raise ValueError("Name can't be empty.")
        self.name = name
        
class Student(Name):
    def __init__(self,name,id):
        super().__init__(name)
        self.id = id
        
class Professor(Name):
    def __init__(self, name,subject):
        super().__init__(name)
        self.subject = subject
        
def main():
    name = Name("Abdul")
    student = Student("AJ",3)
    professor = Professor("JK","CS")
    
if __name__ == "__main__":
    main()