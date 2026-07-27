def main():
    student = get_student_as_dict()
    if student["name"] == "Abdul":
        student["address"] = "California"
    print(f"{student["name"]} is from {student["address"]}")

def get_student_as_dict():
    name = input("Name: ")
    address = input("Address: ")
    return {"name":name,"address":address}

if __name__ == "__main__":
    main()