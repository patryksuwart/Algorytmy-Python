def my_function():
  print("Hello from a function")

my_function()

print()

def my_function2(fname):
  print(fname + " Refsnes")

my_function2("Emil")
my_function2("Tobias")
my_function2("Linus")

print()

def my_function3(fname, lname):
  print(fname + " " + lname)

my_function3("Emil", "Refsnes")

print()

def my_function4(*kids):
  print("The youngest child is " + kids[2])

my_function4("Emil", "Tobias", "Linus")

print()

def my_function5(**kid):
  print("His last name is " + kid["lname"])

my_function5(fname = "Tobias", lname = "Refsnes")