def main():
    menu()

def menu():
    all_student = []
    while True:
        display_choice()
        choice = user_choice()
        match choice:
            case 1:
                add_student(all_student)
                
            case 2:
                view_student(all_student)
                
            case 3:
                search_student(all_student)
                
            case 4:
                delete_student(all_student)
                
            case 5:
                update_student(all_student)
            
            case 6:
                print("Thankyou.")
                break
            
            case _:
                print("Please enter a valid input.")
    
def display_choice():
    print("Choose the choice.")
    print("1.Add Student's.")
    print("2.View Student's.")
    print("3.Search Student's.")
    print("4.Delete Student's.")
    print("5.Update Student detail.")
    print("6.Exit.")
    
def user_choice():
    while True:
        try:
            return int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid choice.")
            
def get_number(prompt):
    while True:
        try:
            n = int(input(prompt))
            if n > 0:
                return n
            print("Enter a number greater than zero.")
        except ValueError:
            print("Please enter a valid input.")
            
def add_student(student_list):
    name = input("Enter your name: ")
    if not student_list:
        student_id = 1
    else:
        student_id = max(s["id"] for s in student_list)
    new_student = {
        "id":student_id,
        "name":name
    }
    student_list.append(new_student)

def view_student(view_st):
    if not view_st:
        print("There is no student list to show!")
    else:
        print("-"*50)
        print("Student's name.")
        for view in view_st:
            print(f'Id: {view["id"]} ,Name: {view["name"]}')
            
def search_student(student_list):
    if not student_list:
        print("There are no student's to search in the list.")
    else:
        search = get_number("Enter the student ID to search: ")
        for student in student_list:
            if student["id"] == search:
                print(f'Student with ID: {student["id"]} and Name: {student["name"]} is in the list.')
                break
        else:
            print(f"Student with ID: {search} is not in the list.")
            
def delete_student(student_list):
    if not student_list:
        print("Nothing to delete as no student are there in the list.")
    else:
        delete = get_number("Enter the student ID to remove student: ")
        for student in student_list:
            if student["id"] == delete:
                student_list.remove(student)
                print("Student successfully removed from the list.")
                break
        else:
            print(f"no student with ID: {delete} exist to remove from the list.")

def update_student(student_list):
    if not student_list:
        print("No such student to update in the list.")
    else:
        update = get_number("Enter the student ID to update student detail's: ")
        for student in student_list:
            if student["id"] == update:
                student["name"] = input("Enter name you want's to: ")
                break
        else:
            print(f"No student with ID: {update} found in the list.")

menu()
