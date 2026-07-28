class Student:
    def __init__(self,name,address):
        self.name = name
        self.address = address
        
def main():
    student = get_student()
    print(f"{student.name} is from {student.address}")

def get_student():
    name = input("Name: ")
    address = input("Address: ")
    return Student(name,address)

if __name__ == "__main__":
    main()
    