def main():
    student = get_student()
    # if student[0] == "Abdul":  
    #     student[1] = "California" -> Tuples are immutable.
    print(f"{student[0]} is from {student[1]}.")
    
    student_list = get_student_as_list()
    if student_list[0] == "Abdul":  
        student_list[1] = "California"
    print(f"{student_list[0]} is from {student_list[1]}.")
    
    
def get_student():
    name = input("Name: ")
    address = input("Address: ")
    return (name,address) # will be returned as a tuple.

def get_student_as_list():
    name = input("Name: ")
    address = input("Address: ")
    return [name,address]

if __name__ == "__main__":
    main()