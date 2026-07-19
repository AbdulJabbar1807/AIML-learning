# Variable
A Variable is a container that is used to store data/values such as text,number,image,videos and many more information in the computer memory.

``` python
    a = 5
    name = "AJ"
```
# DataTypes 
- int : every type of interger numbers.
- float : every type of decimal numbers.
- str : string values.
- bool : Either 'True' or 'False'.
- list : List is a datatype used to store multiple elements in a single variable.
    - Ordered,Mutable and allows Duplicate values.
- dictionary : Dictionaries are the set of key value pairs,label items so that they can be found instantly.

# Function
Function is a reusable block of code that can be used when it is called to perform a specific task.

``` python
    def greet()
        print("hello") 
```
- Paramter : Parameter is a variable defined when a function is created which receives data when function is called.
- Argument : Argument is the actual values passed to a function when it is called.
- Methods : Methods are the built in function associated with objects in python that performs action on those objects.

# Conditionals
Conditional in python allows a program to make decision based on whether the condition is either True or False.

### Comparison Operator
- '>' : greater than 
- '<' : less than
- '>=' : greater than equal to 
- '<=' : less than equal to
- '==' : equal to assignment
- '!=' : not equal

### Conditional statements
- 'if'
- 'elif'
- 'else'

### Logical Operator
- 'or'
- 'not'
- 'and'

# Loops
Loop is a block of code that executes repeatedly until the condition becomes false or the all items in the collection have been processed.
## Types of loops
### While
- A 'while' loop executes a code repeatedly **until the given condition is 'True'**.
- Used to validate input or ask questions.
### For
- A 'For' loop executes a code until all items in a collection[list,string or range] are processed.
- Used to iterate over items,printing number,process through string.

# Exception-handling
## SyntaxError 
- Grammatical mistakes made in the programming language.
``` python
    print("Abdul Jabbar") 'will give a SyntaxError'.
```

## ValueError
- Invalid user input.
``` python
    x = int(input("What's x? "))
    "if user enter's 'ab',it will give a ValueError."
```

## NameError
- if a variable is not defined in the program.
``` python
    print(x) "will give a NameError,as 'x' is not defined."
```
# Libraries
## modules
- Module in python is a library that has many functions or a feature built into it.

### import
- The import keyword in python allows you to import content,features or function's from a module.
``` python
    import random
    coin = random.choice(["heads","tails"])
    print(coin)
```

### from
- The from keyword in python allows you to import a specific content,feature or function from a module.
``` python 
    from random import choice
    coin = choice(["heads","tails"])
    print(coin) 'will generate a 50-50 chances of heads and tails.
```
## packages
- Packages are the thrid party libraries that can be used to access many functions,features,etc.
    - to get this packages,these can be downloaded from PYPi Python Packages Index (pypi.org).
    - pip an built in packages installer in python.
    ``` python
        pip install cowsay
    ```

# Unit-test
## Pytest 
- Pytest is a python package that allows you to test function's working by checking all the possible cases as well as corner cases.

# File Input/Output
## Open 
- Open keyword in python allows us to open a text file where we can save data from python file in computer's memory.

## With-Statement
- 'With' statement in python allows us to open a file and automatically closes and save the '.txt' file.

## Sorted
- Sorted is a built in python method allows us to sort '.txt' file in alphabetical order.
    