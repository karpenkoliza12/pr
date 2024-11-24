# my_dict = {'liza': 2000, 'Sasha': 1996}
# print(my_dict)
# print(my_dict['liza'])
# print(my_dict.get('Masha'))
# my_dict.update({'Misha': 2005, 'Lena': 1979})
# a = my_dict.pop('Sasha')
# print(a)
# print(my_dict)
#
# my_set = {1, 2, 1, 'liza', 'Liza'}
# print(my_set)
# my_set.add(5)
# my_set.add(6)
# my_set.remove(1)
# print(my_set)

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = list(students)
average_value = [sum(i) / len(i) for i in grades]
average_score = dict(zip(sorted(students), average_value))

print(average_score)