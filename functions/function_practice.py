# Main function.
def main():
    name = input("What's the name? ").strip().title()
    hello(name)
    
    language = input("What's your favorite language? ").strip().capitalize()
    favorite_language(language)
    
    num1 = int(input("Enter the number to square : "))
    print(f"Squared : {square(num1)}")
    
    num2 = int(input("Enter the number to cube : "))
    print(f"Cubic : {cube(num2)}")
    
    print(full_name(name))

   
#Q1. Greeting user.
def hello(name):
    print(f"hello, {name}")
    
    
#Q2. Favourite programming language.
def favorite_language(language="Arabic"):
    print(f"Favorite language is {language}.")
    
#Q3. Square number
def square(x):
    return pow(x,2)

#Q4. Cube number
def cube(x):
    return x ** 3

#Q5. Full name
def full_name(name):
    first,last = name.split(" ")
    return f"{first} {last}"
    

main()