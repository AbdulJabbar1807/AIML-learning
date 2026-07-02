students = ['Abdul','Jabbar','Khokhar']

search_st = input("Enter the student you want to search in list: ").title()
found = False
for search in students:
    if search_st == search:
        found = True
        break
if found:
    print("found")
else:
    print("Not found")
        
        
