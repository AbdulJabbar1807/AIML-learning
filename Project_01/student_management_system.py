import sys
import csv

def main():
    all_student = []
    menu(all_student)
       
def menu(all_student):
    while True:
        display_choice()
        choice = user_choice()
        match choice:
            case 1:
                name = get_name("Enter the Student's Name: ")
                add_student(all_student,name)
                
            case 2:
                view_student(all_student)
                
            case 3:
                search = get_number("Enter the student ID to search: ")
                search_student(all_student,search)
                
            case 4:
                delete = get_number("Enter the student ID to remove student: ")
                delete_student(all_student,delete)
                
            case 5:
                update = get_number("Enter the student ID to update student detail's: ")
                name = get_name("What's the Student Name to update: ")
                update_student(all_student,update,name)
            
            case 6:
                students_details_csv(all_student) 
                print("Thankyou for using SMS.")
                print("Successfully shutdown the system.")
                sys.exit()
            
            case _:
                print("Please choose from the given choice's.")
    
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
            
def students_details_csv(student_list):
    with open("student_management_system.csv","w",newline="") as file:
        writer = csv.DictWriter(file,fieldnames=["id","name"])
        writer.writeheader()
        writer.writerows(student_list)
            
def get_number(prompt):
    while True:
        try:
            n = int(input(prompt))
            if n > 0:
                return n
            print("Enter a number greater than zero.")
        except ValueError:
            print("Please enter a valid input.")
            
def get_name(prompt):
    while True:
            n = input(prompt).title().strip()
            if n.replace(" ","") == "":
                print("Name cant be empty!")
            elif n.replace(" ","").isalpha():
                return n
            else:
                print("Please enter alphabetical letter's only.")
                
            
def add_student(student_list,name):
    if not student_list:
        student_id = 1
    else:
        student_id = max(s["id"] for s in student_list) + 1
    new_student = {
        "id":student_id,
        "name":name
    }
    student_list.append(new_student)

def view_student(view_st):
    if not view_st:
        print("There is no student list to show!")
    else:
        print("Student's Info-")
        print("ID     Name")
        print("-"*50)
        for view in view_st:
            print(f'{view["id"]}     {view["name"]}')
            
def search_student(student_list,search):
    if not student_list:
        print("There are no student's to search in the list.")
    else:
        for student in student_list:
            if student["id"] == search:
                print(f'Student with ID: {student["id"]} and Name: {student["name"]} is in the list.')
                break
        else:
            print(f"Student with ID: {search} is not in the list.")
            
def delete_student(student_list,delete):
    if not student_list:
        print("Nothing to delete as no student are there in the list.")
    else:
        for student in student_list:
            if student["id"] == delete:
                student_list.remove(student)
                print("Student successfully removed from the list.")
                break
        else:
            print(f"no student with ID: {delete} exist to remove from the list.")

def update_student(student_list,update,name):
    if not student_list:
        print("No such student to update in the list.")
    else:
        for student in student_list:
            if student["id"] == update:
                student["name"] = name
                break
        else:
            print(f"No student with ID: {update} found in the list.")

if __name__ == "__main__":
    main()
