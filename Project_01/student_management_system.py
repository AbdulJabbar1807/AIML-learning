import sys
import csv
import re

def main():
    all_students = []
    read_students_details_csv(all_students)
    menu(all_students)
       
def menu(all_students):
    while True:
        display_choice()
        choice = user_choice()
        match choice:
            case 1:
                name = get_name("Enter the Student's Name: ")
                email = get_email("What's your email address: ")
                add_student(all_students,name,email)
                
            case 2:
                view_student(all_students)
                
            case 3:
                search_id = get_number("Enter the student ID to search: ")
                search_student(all_students,search_id)
                
            case 4:
                delete_id = get_number("Enter the student ID to remove student: ")
                delete_student(all_students,delete_id)
                
            case 5:
                update_id = get_number("Enter the student ID to update student detail's: ")
                name = get_name("What's the Student Name to update: ")
                update_student(all_students,update_id,name)
            
            case 6:
                write_students_details_csv(all_students) 
                print("Thank you for using SMS.")
                print("Successfully shutdown the system.")
                sys.exit()
            
            case _:
                print("Please choose from the given choice's.")
    
def display_choice():
    print("Main Menu.")
    print("1.Add Students.")
    print("2.View Students.")
    print("3.Search Students.")
    print("4.Delete Students.")
    print("5.Update Students Name.")
    print("6.Exit.")
    
def user_choice():
    while True:
        try:
            return int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid choice.")
            
def write_students_details_csv(student_list):
    with open("student_management_system.csv","w",newline="") as file:
        writer = csv.DictWriter(file,fieldnames=["id","name","email"])
        writer.writeheader()
        writer.writerows(student_list)
        
def read_students_details_csv(student_list):
    try:
        with open("student_management_system.csv","r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                student_list.append({"id":int(row["id"]),"name":row["name"],"email":row["email"]})          
    except FileNotFoundError:
        print("There is no file to view.")        
    
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
        name = input(prompt).strip().title()
        if re.search(r"^[a-zA-Z]?[a-zA-Z ]+'?$",name):
            return name
        else:
            print("Please enter name in alphabetical letters only!")
        
def get_email(prompt):
    while True:
        email = input(prompt)
        if re.search(r"^[a-z0-9_\.]+@[a-z0-9]+\.([a-z0-9-]+\.)?(com|gov|in|edu|org)$",email,re.IGNORECASE):
            return email
        print("Please enter a valid email address.")
                 
def add_student(student_list,name,email):
    if not student_list:
        student_id = 1
    else:
        student_id = max(s["id"] for s in student_list) + 1
    new_student = {
        "id":student_id,
        "name":name,
        "email":email
    }
    student_list.append(new_student)

def view_student(view_student):
    if not view_student:
        print("There is no student list to show!")
    else:
        print("Students Info-")
        print(f"{"ID":<6}{"Name":<25}{"Email":<20}")
        print("-"*70)
        for view in view_student:
            print(f'{view["id"]:<6}{view["name"]:<25}{view["email"]:<20}')
            
def search_student(student_list,search):
    if not student_list:
        print("There are no student's to search in the list.")
    else:
        for student in student_list:
            if student["id"] == search:
                print(f'Student with ID: {student["id"]} and Name: {student["name"]} is in the list.')
                break
        else:
            print(f"Student with ID {search} is not in the list.")
          
def delete_student(student_list,delete):
    if not student_list:
        print("Nothing to delete as no student are there in the list.")
    initial_list = len(student_list)
    student_list[:] = [s for s in student_list if s["id"]!=delete]
    if len(student_list)<initial_list:
        print(f"Student with ID {delete} removed successfully.")
    else:
        print(f"No student with ID {delete} exist in the list.")

def update_student(student_list,update,name):
    if not student_list:
        print("No such student to update in the list.")
    else:
        for student in student_list:
            if student["id"] == update:
                student["name"] = name
                break
        else:
            print(f"No student with ID {update} found in the list.")

if __name__ == "__main__":
    main()
