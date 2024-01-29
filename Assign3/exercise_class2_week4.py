## Q1
sample_tuple = ('a', 'c', 'b', 'd', 'd', 'a', 'e', 'a', 'e')
    
char_count = {}
for char in sample_tuple:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

char_count = dict(char_count.items())
print("dict =",char_count) #dict = {'a': 3, 'c': 1, 'b': 1, 'd': 2, 'e': 2}

## Q2
roll_number = [47, 64, 69, 37, 76, 83, 95, 97] 
new_roll_number = []

sample_dict = {
    'Jhon':47,
    'Emma':69,
    'Kelly':76,
    'Jason':97
    }

for number in roll_number: 
    for value in sample_dict.values():
        if number == value:
            new_roll_number.append(number)
new_roll_number = set(new_roll_number)
print(new_roll_number) #{97, 76, 69, 47}

## Q3
speed ={'jan':47, 'feb':52, 'march':47, 'April':44, 'May':52, 'June':53, 'july':54, 'Aug':44, 'Sept':54}
new_list = list(set(speed.values()))
print(new_list) #[44, 47, 52, 53, 54]
