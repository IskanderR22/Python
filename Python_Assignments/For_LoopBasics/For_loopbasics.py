
for i in range(0, 151):
    print(i)
    
    
for i in range(5, 1001):
    if i % 5 == 0:
        print(i)


for i in range(1, 101):
    if i % 10 == 0:
        print("CodingDojo")
    elif i % 5 == 0:
        print("Coding")
        

sum_of_odds = 0
    
for i in range(0, 500001):
    if i % 2 != 0:
        sum_of_odds += i

print(sum_of_odds)


for i in range(2018, 0, -4): 
    print(i)    

low_num = 2
high_num = 10
mult = 2

for i in range(low_num, high_num):          
    if i % mult == 0:
        print(i)