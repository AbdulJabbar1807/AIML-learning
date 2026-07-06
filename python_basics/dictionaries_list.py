student_details = [
    {"name":"Abdul","Age":20},
    {"name":"Jabbar","Age":21},
    {"name":"Khokhar","Age":22}
]
for student in student_details:
    print(student["name"])
    
for age in student_details:
    print(age["Age"])
    
for detail in student_details:
    print(f"Name: {detail["name"]} and Age: {detail["Age"]}")