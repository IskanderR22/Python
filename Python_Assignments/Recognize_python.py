- variable declaration 
- log statement 
- type check
- length check
- comment
    - single line 
    - multiline 
- Data Types 
    - Primitive
        - Boolean 
        - Numbers 
        - Strings 
    - Composite
        - List  
            - initialize 
            - access value 
            - change value 
            - add value 
            - delete value 
        - Tuples 
            - initialize 
            - access value
            - change value 
            - add value    
            - delete value 
                    
        - Dictionary
            - initialize
            - access value
            - change value
            - add value
            - delete value
- conditional
    - if
    - else if
    - else
- for loop
    - start
    - stop
    - increment
    - break
    - continue
    - sequence
- while loop
    - start
    - stop
    - increment
- function
    - parameter
    - argument
    - return

* Bonus: Errors

- NameError: name <variable name> is not defined
- TypeError: 'tuple' object does not support item assignment
- KeyError: 'favorite_team'
- IndexError: list index out of range
- IndentationError: unexpected indent
- AttributeError: 'tuple' object has no attribute 'pop'
- AttributeError: 'tuple' object has no attribute 'append'
- Tuples
    - change value
    - add value
    - delete value
    
    ########################
    
    num1 = 42 # Declaring a Varible name / value
num2 = 2.3 # Var num2 = 2.3
boolean = True # Data type that can be defined as true or false
string = 'Hello World' # Length is 10
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # List
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # List
fruit = ('blueberry', 'strawberry', 'banana') # Tuple
print(type(fruit)) # Prints the different types of fruit
print(pizza_toppings[1]) # Prints the value at index 1
pizza_toppings.append('Mushrooms') # Adds Muchrooms to the pizza.toppings list
print(person['name']) # Prints John
person['name'] = 'George' # Changes the name from John to George
person['eye_color'] = 'blue' 
print(fruit[2]) # Prints banana

if num1 > 45:
    print("It's greater")
else:
    print("It's lower") # Will print it's lower

if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!") # Will print Just right!

for x in range(5):
    print(x)
for x in range(2,5):
    print(x)
for x in range(2,10,3):
    print(x)
x = 0
while(x < 5):
    print(x)
    x += 1 # Wikll print 1, 2, 3, 4 

pizza_toppings.pop() # Will remove the value at the end of the list
pizza_toppings.pop(1) # Will remove the value at index 1

print(person) # 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False
person.pop('eye_color') # Will remove the eye_color information
print(person) # 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break

def print_hello_ten_times():
    for num in range(10):
        print('Hello')

print_hello_ten_times()

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3) Prints the value stored in num3
# num3 = 72 Sets Var num3 to 72
# fruit[0] = 'cranberry' Set the value at index 0 to Cranberry
# print(person['favorite_team']) 
# print(pizza_toppings[7]) Will print the value at index 7 and print false
#   print(boolean)
# fruit.append('raspberry') addes raspbeery to the fruit list
# fruit.pop(1) Removes the value at index 1