immutable_var = (1, 2, 'help', True, [1,5])
print(immutable_var)
#immutable_var[0] = 3 – нельзя изменить, т.к. кортеж неизменяимый тип данных
mutable_list = [1, 2, 'help', True, [1,5]]
mutable_list[0],mutable_list[1],mutable_list[2] = 4, 5, 'stop'
print(mutable_list)