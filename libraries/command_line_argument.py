import sys 
# sys.argv
# if len(sys.argv) < 2:
#     print("Too few arguments")
# elif len(sys.argv) > 2:
#     print("Too many arguments")
# else:
#     print("I'm",sys.argv[1])

# Using sys.exit
# if len(sys.argv) < 2:
#     sys.exit("Too few arguments")
# elif len(sys.argv) > 2:
#     sys.exit("Too many arguments")

# print("I'm",sys.argv[1])

# Using for-loop to iterate over multiple arguments.
if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv:
    print(arg)