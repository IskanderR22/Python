#1
def number_of_food_groups():
    return 5
print(number_of_food_groups()) # Print the number 5



#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches()) # Will print 5 Is this an error?


#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold()) # Will print 5 once a return command is reached, the function stops.


#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers()) # Will only print 5, return will not run any code after it


#5
def number_of_great_lakes():
    print(5)                # Will print 5 when the function is called
x = number_of_great_lakes() 
print(x)                    # Will print none, no value was returned to the function 


#6
def add(b,c):
    print(b+c) # Will print 3 , 5 
print(add(1,2) + add(2,3)) # Will not add together because there was no value returned


#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))  # Will print 25, no spaces 


#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)        # Will print 100
    if b < 10:
        return 5    # b is 100 
    else:
        return 10   # b is 100, so the function returns 10
    return 7
print(number_of_oceans_or_fingers_or_continents())  # Will print 10 


#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7 # When b is less than c the function will stop and return 7
    else:
        return 14 # If b is greater than c return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3)) # Will print 7
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3)) # Will print 14
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3)) 
# Will print 7 14 21


#10
def addition(b,c):
    return b+c # Will return the value of b + c
    return 10 # Will not run because there is a return above it 
print(addition(3,5)) # Will print 8


#11
b = 500 # Set the value of b to 500
print(b) # Will print 500
def foobar(): 
    b = 300
    print(b)
print(b) # Will print 500
foobar() # Calls the function and will print 300
print(b) # Will print 500


#12
b = 500
print(b) # Will print 500
def foobar():
    b = 300
    print(b)
    return b # Will return 300 to the function
print(b) # Will print 500
foobar() # Will print 300
print(b) # Will print 500


#13
b = 500
print(b) # Will print 500
def foobar():
    b = 300
    print(b)
    return b
print(b) # Will 500
b=foobar() # Sets the value of b to the return value of the function and print 300
print(b) # Will print 300


#14
def foo():
    print(1) # Will print 1 
    bar()
    print(2) # Will print 2
def bar():
    print(3) # Will print 3 
foo()  # Calls the foo() function and will call on the bar() functions, will print 1 3 2


#15
def foo(): 
    print(1) # Will print 1
    x = bar() # Sets the value of x to the return value of ther bar() function 
    print(x) # Will print 5
    return 10 # Returns 10 to the value of foo()
def bar():
    print(3) # Will print 3
    return 5 # Will return 5 to the value of the bar() function 
y = foo() # Will set the value of y to the return value of the function foo(), so the new value is 10
print(y) # Will print 10