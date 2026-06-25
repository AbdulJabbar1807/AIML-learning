def main():
    age = int(input("What's your age: "))
    print(user_age(age))
        
    print(can_drive(age))
    
    num1 = int(input("What's the number: "))
    print(check_number(num1))
    
    num2 = int(input("What's the number: "))
    print(largest_number(num1,num2))
    
    op = str(input("choose operation (+,-,*,/,%): "))
    print(calculator(num1,num2,op))
    
    if is_even(op):
        print("'Even'")
    else:
        print("'Odd'")
        
    score = int(input("Enter your score: "))
    print(grade(score))
    
    temp = int(input("What's the temperature (in Celcius)? "))
    print(temperature_checker(temp))
    
    country = str(input("What's your country name? "))
    print(country_check(country))
    
    day = str(input("Which day? "))
    print(day_checker(day))
    
    option = int(input("Choose option: "))
    print(menu(option))

# Q1. User's age group.
def user_age(age):
    if age <= 12:
        return "'Child'"
    elif age <= 19:
        return "'Teenager'"
    elif age <=60:
        return "'Adult'"
    else:
        return "'Senior'"

#Q2. Check Number - Positive,Negative or Zero.
def check_number(num1):
    if num1 > 0:
        return f"'Positive'"
    elif num1 < 0:
        return f"'Negative'"
    else:
        return f"'Zero'"
    
#Q3. Voter eligibility-
def voter_eligibility(age):
    return True if age >=18 else False

#Q4. largest number-
def largest_number(num1,num2):
    if num1>num2:
        return f"'{num1}' is the largest number. "
    else:
        return f"'{num2}' is the largest number."
    
#Q5. Even or Odd-
def is_even(n):
    return True if n % 2 == 0 else False
    
#Q6. Grade calculator-
def grade(score):
    if score < 0 or score > 100:
        return f"Invalid input."
    elif score>=90:
        return f"'A'"
    elif score>80:
        return f"'B'"
    elif score>70:
        return f"'C'"
    elif score>60:
        return f"'D'"
    elif score>50:
        return f"'E'"
    else:
        return f"F"
    
#Q7. Tempreature checker-
def temperature_checker(temp):
    if temp >= 35:
        return f"'Hot'"
    elif temp >=15:
        return f"'Sunny'"
    else:
        return f"'Cold'"
    
#Q8. Driving eligibility-
def can_drive(age):
    if age>70:
        return f"'Drive carefully'"
    elif age>=18:
        return f"Yes,you can drive."
    else:
        return f"No,you can't drive."
    
#Q9. Country checker-
def country_check(country):
    match country.title():
        case "India":
            return f"New Delhi"
        case "America":
            return f"Washington,D.C."
        case "Saudi Arabia":
            return f"Riyadh"
        case "UAE":
            return f"Abu Dhabi"
        case "Britain":
            return f"London"
        case _:
            return f"Unknown country"
            
#Q10. Day checker-
def day_checker(day):
    match day.title():
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return f"Weekdays"
        case "Saturday" | "Sunday":
            return f"Weekends"
        case _:
            return f"Unknown input"
        
#Q11. Menu-
def menu(x):
    match x:
        case 1:
            return f"Add Student"
        case 2:
            return f"Delete Student"
        case 3:
            return f"Update Student"
        case _:
            return f"Invalid input"
        
#Q12. Calculator-
def calculator(num1,num2,op):
    match op:
        case '+': 
            return f"{num1+num2}"
        case '-': 
            return f"{num1-num2}"
        case '*': 
            return f"{num1*num2}"
        case '/': 
            return f"{num1/num2}"
        case '%': 
            return f"{num1%num2}"
        case _: 
            return f"Invalid Input."
      
  
main()
    



    