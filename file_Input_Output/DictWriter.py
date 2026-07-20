import csv
name = input("What's your name: ")
home = input("Enter your home address: ")

with open("students_DictWriter.csv","a") as file:
    writer = csv.DictWriter(file,fieldnames=["name","home"])
    writer.writerow({"name":name,"home":home})