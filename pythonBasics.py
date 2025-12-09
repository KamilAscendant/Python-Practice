#data types
print("\n=== DATA TYPES ===")
print()

#Int
test_int = 10

#Float 
test_float = 10.0

#String
test_string = "Hello World"

#Boolean
test_boolean = True

#Print to Console
print("\n=== PRINT TO CONSOLE ===")
print()
print(test_string)

#Input
print("\n=== INPUT ===")
print()

#name = input("Enter your name: ")

#Python always returns floats for division
print("\n=== DIVISION ===")
print() 
x = 5
y = 3
print(x / y)
#Use // for integer division
print(x // y)

#Methods
print("\n=== STRING METHODS ===")
print()
test_string_lower = test_string.lower()
print(test_string_lower)
test_string_upper = test_string.upper()
print(test_string_upper)
print(test_string.capitalize())
print(test_string.lower().count("o"))

#String Multiplication and Addition
print("\n=== STRING MULTIPLICATION AND ADDITION ===")
print()
print(test_string * 3)
print(test_string + " woah")

#Conditional Operators
print("\n=== CONDITIONAL OPERATORS ===")
print()

# ==, !=, >, <, >=, <=
print ('a' > 'b') # compares ASCII values
print (ord('a')) # prints ASCII value of 'a'
print (ord('b')) # prints ASCII value of 'b'

#Chained Conditionals
print("\n=== CHAINED CONDITIONALS ===")
print()
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
print("\n=== IF, ELIF, ELSE STATEMENTS ===")
print()
name = input("Enter your name: ")
if name.lower() == "karma":
    print("Greetings, Captain!")
elif name.lower() == "ailsa":
    print("Hello, Stinky!")
else:
    print("Greetings, private " + name)

#Collections - Lists
print("\n=== COLLECTIONS - LISTS ===")
print()
test_list = [1, 2, True, 'Hello']
print (test_list)
print (test_list[0]) #Accessing first element   
print (len(test_list)) #Length of list
test_list.append(3.5) #Adding element to list
test_list.extend([4, 5, 6]) #Extending list with another list
print (test_list)
test_list.remove(True) #Removing element from list
print (test_list)
print (test_list.index(5)) #Finding index of element in list
print (test_list.pop())   #Removing and returning last element of list
print (test_list.pop(2)) #Removing and returning element at index 2
print (test_list)
test_list.insert(2, 'New Element') #Inserting element at index 2
print (test_list)
#tuples are immutable lists

#for loops
print("\n=== FOR LOOPS ===")
for i in range (1, 5, 1):
    print("Iteration:", i)

for i in test_list:
    print("Element:", i)

for i, element in enumerate(test_list):
    print("Index:", i, "Element:", element)

#while loops
print("\n=== WHILE LOOPS ===")

count = 0
while count < 5:
    print("Count is:", count)
    count += 1

#slice operator
print("\n=== SLICE OPERATOR ===")
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
y = ["hi", "hello", "greetings", "salutations"]
s = "hello"

sliced = x[0:5:2]  #slicing with start:stop:step
print("Sliced list:", sliced)
sliced_y = y[1:4]  #slicing with start:stop
print("Sliced y:", sliced_y)
sliced_s = s[0:4]  #slicing string
print("Sliced s:", sliced_s)
sliced_reverse = x[::-1]  #reversing list
print("Reversed x:", sliced_reverse)

#Sets
print("\n=== SETS ===")
test_set = set()
test_set.add(1)
test_set.add(4) 
test_set.add(3)
print("Initial set:", test_set)
test_set.add(6)  #adding element
print("After adding 6:", test_set)
test_set.remove(3)  #removing element
print("After removing 3:", test_set)
print("Contains 4:", 4 in test_set)  #checking membership
print("Contains 3:", 3 in test_set)  #checking membership
test_set_2 = {4, 5, 6, 7}
union_set = test_set.union(test_set_2)  #union of sets
print("Union with {4,5,6,7}:", union_set)
intersection_set = test_set.intersection(test_set_2)  #intersection of sets
print("Intersection with {4,5,6,7}:", intersection_set)

#Dictionaries
print("\n=== DICTIONARIES ===")
test_dict = {'key': 4}
print(test_dict['key'])
test_dict['new_key'] = 10  #adding new key-value pair
print(test_dict)
print("Keys:", test_dict.keys())  #printing all keys
print("Values:", list(test_dict.values()))  #printing all values
for key, value in test_dict.items():  #iterating through key-value pairs
    print("Key:", key, "Value:", value) 
print("Contains 'key':", 'key' in test_dict)  #checking membership
print("Contains 'missing_key':", 'missing_key' in test_dict)  #checking membership

for key, value in test_dict.items():  #iterating through key-value pairs
    print("Key:", key, "Value:", value)

#Comprehensions
print("\n=== COMPREHENSIONS ===")
a = [a + 5 for a in range(5)]
print("List comprehension:", a)
b = {b: b  for b in range(100) if b % 10 == 0}
print("Dictionary comprehension:", b)
tuple_comp = tuple(c * 2 for c in range(5))
print("Tuple comprehension:", tuple_comp)

#functions
print("\n=== FUNCTIONS ===")
def greet(name):
    print("Hello, " + name + "!")
    def add(a, b):
        return a + b
    print("2 + 3 =", add(2, 3))
print(greet("Karma"))

#*args and **kwargs
print("\n=== *ARGS AND **KWARGS ===")
def func(*args, **kwargs):
    pass
j = [1, 23, 2333, 2323]
print(*x)  #unpacking list - unpacks whatever we have in a collection and sends them through as args to a collection

def func(o, p):
    print(o,p)
pairs = [(2,3), (4,5), (6,7)]
for pair in pairs:
    func(*pair)  #unpacking each tuple in the list and sending them as separate args to the function

#exception handling
print("\n=== EXCEPTION HANDLING ===")
#raise Exception("This is an exception")
try:
    x = 5 / 0
except Exception as e:
    print("Caught an exception:", e)
finally:
    print("This block always executes.")

#Lambda Functions
print("\n=== LAMBDA FUNCTIONS ===")
h = lambda h: h+5
print("Lambda function result:", h(10))

#map, filter, reduce
print("\n=== MAP, FILTER, REDUCE ===")
nums = [1, 2, 3, 4, 5]
mp = map(lambda l: l * 2, nums)
print("Map result:", list(mp))
flt = filter(lambda m: m % 2 == 0, nums) #returns true or false based on whether the element should be included
print("Filter result:", list(flt)) 

#FStrings
print("\n=== FSTRINGS ===")
name = "Karma"
age = 25
print(f"My name is {name} and I am {age} years old.")
