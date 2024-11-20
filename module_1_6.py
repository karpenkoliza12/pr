my_dict = {'liza': 2000, 'Sasha': 1996}
print(my_dict)
print(my_dict['liza'])
print(my_dict.get('Masha'))
my_dict.update({'Misha': 2005, 'Lena': 1979})
a = my_dict.pop('Sasha')
print(a)
print(my_dict)

my_set = {1, 2, 1, 'liza', 'Liza'}
print(my_set)
my_set.add(5)
my_set.add(6)
my_set.remove(1)
print(my_set)

