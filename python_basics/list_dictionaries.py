# lists in dictionaries
student = {
    "name":"Abdul Jabbar",
    "skills":["Python","C++","Java","SQL"]
}
print(student["skills"][3])
student["skills"].append("Machine learning")
for st in student["skills"]:
    print(st)
    
count = len(student["skills"])
print(count)