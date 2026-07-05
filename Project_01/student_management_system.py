def main():
    menu()

def menu():
    while True:
        display_menu()
        choice = user_choice()
    
        match choice:
            case 1:
                total_st = get_number()
                students_name(total_st)

            case 2:
                print("Thankyou")
                break
            
            case _:
                print("Invalid choice try again!")
    
    
def display_menu():
    print("Choose option's-")
    print("1.Student's list")
    print("2.Exit")
    
def user_choice():
    return int(input("Enter your choice: "))

def get_number():
    while True:
        n = int(input("Enter number: "))
        if n>0:
            return n
        else:
            print("Invalid number,try again.")

def students_name(total_st):
    students = []
    for _ in range(total_st):
        name = input("Enter your name: ")
        students.append(name)
        
    print("'Student's name'")
    print("-"*40)
    
    for i in range(len(students)):
        print(f"{i+1}. {students[i]}")
        
    search_st = input("Enter the student you want to search in list: ").strip().title()
    found = False
    for search in students:
        if search == search_st:
            found = True
            break
    if found:
        print(f"{search_st} is in the list.")
    else:
        print(f"{search_st} is not in the list.")
        

main()