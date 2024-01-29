## Q4

my_list = [1, 2, 3, 4, 5, 6]


def dict_list(my_list):
    if len(my_list) == 1:
        return my_list[0]

    return {my_list[0]: dict_list(my_list[1:])}

result = dict_list(my_list)
print(result)


























##    
####    if not my_list:
####        return {}
##
##    if len(my_list) >= 1:
##        print(my_list[0])#return my_list[0]
##
##    return my_list[0] #{my_list[0]: dict_list(my_list[1:])}
##
##
##result = dict_list(my_list)
###print(result)
