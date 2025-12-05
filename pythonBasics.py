#data types

#Int
test_int = 10

#Float 
test_float = 10.0

#String
test_string = "Hello World"

#Boolean
test_boolean = True

#Print to Console
print(test_string)

#Input
#name = input("Enter your name: ")

#Python always returns floats for division 
x = 5
y = 3
print(x / y)
#Use // for integer division
print(x // y)

#Methods
test_string_lower = test_string.lower()
print(test_string_lower)
test_string_upper = test_string.upper()
print(test_string_upper)
print(test_string.capitalize())
print(test_string.lower().count("o"))

#String Multiplication and Addition
print(test_string * 3)
print(test_string + " woah")

#Conditional Operators
# ==, !=, >, <, >=, <=
print ('a' > 'b') # compares ASCII values
print (ord('a')) # prints ASCII value of 'a'
print (ord('b')) # prints ASCII value of 'b'

#Chained Conditionals
x = 5
y = 8
z = 0

result1 = x == y
result2 = x > x
result3 = z < x+2
result4 = result1 or result2 or result3
print("result4:", result4)
result5 = result4 and result3
print("result5:", result5)

#If, Elif, Else Statements
name = input("Enter your name: ")
if name == "Karma":
    print("Greetings, Captain!")
elif name == "Ailsa":
    print("Hello, Stinky!")
else:
    print("Greetings, private " + name)