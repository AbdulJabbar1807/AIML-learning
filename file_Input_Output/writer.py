import csv

name = input("Enter your name: ")
home = input("Enter your name: ")

with open("students_writer.csv","a") as file:
    writer = csv.writer(file)
    writer.writerow([name,home])