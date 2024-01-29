## Q3

people_list = [['John', 'Doe'], ['Jane'], ['Michael', 'Smith']]

j = 0
i = 0

while j < len(people_list):
    if i < len(people_list[j]):
        people = people_list[j][i]
        print(people, end=' ')
        i += 1
    else:
        j += 1
        i = 0
        print()
