## Q2

A = {1, 2, 3, 7, 9, 12, 15, 18, 21, 24} 
B = {4, 5, 6, 10, 11, 13, 16, 19, 22, 25}

my_list = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 7, 9, 12, 15, 18, 21, 24, 10, 11, 13, 16, 19, 22, 25, 1, 2, 3, 4, 5]

happiness = 0

for i in range(len(my_list)):
    for item in A:
        if my_list[i]== item:
            happiness += 1 #total = 16
for i in range(len(my_list)):
    for item in B:
        if my_list[i]== item:
            happiness -= 1 #total = 13
            
print(happiness) # diff = 3
