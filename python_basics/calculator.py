# Interger inputs
x = int(input("Enter the value of x : "))
y = int(input("Enter the value of y : "))

print("Interger operations")
print(f"Sum : {x+y}")
print(f"Difference : {x-y}")
print(f"multiple : {x*y}")
print(f"Division : {x/y}")
print(f"remainder : {x%y}")

# Float inputs
a = float(input("Enter the value of a : "))
b = float(input("Enter the value of b : "))

print("\nFloat operations")
print(f"Sum of : {a+b}")
print(f"Difference : {a-b}")
print(f"multiple : {a*b}")
print(f"Division : {a/b}")
print(f"remainder : {a%b}")

# Rounding up values.
p = float(input("Enter the value of p : "))
q = float(input("Enter the value of q : "))

r = p+q

print(f"{r:,}")
print(round(r,2))