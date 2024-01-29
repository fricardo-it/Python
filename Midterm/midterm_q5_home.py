## Q5

char_count = {}

def dict_list(my_list):
    if len(my_list) == 1:
        return my_list[0]

    return {my_list[0]: dict_list(my_list[1:])}

def count_list(my_list):
    for char in my_list:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return dict(char_count.items())

my_string = input("Enter a string: ") #Weekend"

result = count_list(my_string)
print(result)


#### Q4
##
##my_list = [1, 2, 3, 4, 5, 6]
##
##
##def dict_list(my_list):
##    if len(my_list) == 1:
##        return my_list[0]
##
##    return {my_list[0]: dict_list(my_list[1:])}
##
##result = dict_list(my_list)
##print(result)

