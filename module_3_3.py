def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [1, 'scasc', [1,2,3]]

values_dict = {'a': 1, 'b': 'ewe', 'c': [1, 2, 2]}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [1, 'dff']
print_params(*values_list_2, 42)