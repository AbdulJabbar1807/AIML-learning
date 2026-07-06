# lists in dictionaries

# student = {
#     "name":"Abdul Jabbar",
#     "skills":["Python","C++","Java","SQL"]
# }
# print(student["skills"][3])
# student["skills"].append("Machine learning")
# for st in student["skills"]:
#     print(st)
    
# count = len(student["skills"])
# print(count)

doctors = {
    "year":2026,
    "name1":["David","MBBS","MD","DM"],
    "name2":["John","MBBS","MS"]
}

print(f"Year: {doctors['year']}")

for detail in doctors["name1"]:
    print(detail,end=" ")