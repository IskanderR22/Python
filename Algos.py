# Variables
    #Containers / stores data 
    #Vary / assign data

hello = "hello there!"

# What is a valid variable name to the computer

is_this_a_valid_variable_name = "Hello!" # Yes it is

faksjbfasjkdfbasdfbajhsdfbhas = "Hello!" # Also valid but not a good one

# - Naming conventions 
# Python naming convention for varibles is snake case
    # All lower case
    # Words sepereated by an underscore 

first_name = "Iskander"
last_name = "Rangel"
age = 26

# Variable names should describe the data the variable holds 
good_game = "Stardew Valley"


# Data Type

# Primitive types
# Integers 
2345
# Strings are just text
"Hello" 
'There' # Single quotes can be used.
# Booleans
True
False
# Floats
3.5
18.7

# Composite Types / Collections / Data structures 
# Lists / The same as JavaScript Arrays
    # Access the information via index / First index is 0
    # Good practice is all data in a list is the same data type, Python lets us put different kinds
[22, 16, "Numbers", True]
# Tuples 
    # Access the information via index / First index is 0
    # Immutable / Once made it cannot be changed
(22, 16, "Numbers", True)
# Dictionaries / The same as JavaScript objects
    # Key / Value pairs
    # ALL KEYS ARE STRINGS
person1 {
    # This is     # Value pairs
    # the key 
    "first_name": "Iskander",
    "last_name": "Rangel",
    "age": 26,
    "interests": ["Games", "Piano", "Music"]
}

# Conditionals

if x > y: # Do not need () or {} when creating the statments 
    # Do something
elif y > x:
    # Do something for the elif, same as else if
else: 
    # Do something for the else 

# &&, ||, ! in Python is translated to and, or, not

# Loops  
# for loops with range
for i in range(5): # Will start at 0 and go up to 4 not 5! This is a single number in the range function
    print("Hello") # This will print Hello 5 times 

for i in range(5,10): # Will start at 5 and stop at 9, not 10! This is a double number in range, start and stop
    print("Hey!")

for i in range(5,10,2): # Will start at 5 and stop at 9, going by 2 every step. This is a triple number in range, start, stop and step!!!
    print("Whoa!")

