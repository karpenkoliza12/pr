from sys import *

setrecursionlimit(3000)
def calculate_structure_sum(structure):
    cnt = 0


    if isinstance(structure, list) and structure != []:
        element = structure[0]
        if isinstance(element, int) or isinstance(element, float):
            return cnt + element + calculate_structure_sum(structure[1:])
        elif isinstance(element, list) and element != []:
            return cnt + calculate_structure_sum(element) + calculate_structure_sum(structure[1:])
        elif isinstance(element, str):
            return cnt + len(element) + calculate_structure_sum(structure[1:])
        elif isinstance(element, set) or isinstance(element, tuple):
            element = list(element)
            return cnt + calculate_structure_sum(element) + calculate_structure_sum(structure[1:])
        elif isinstance(element, dict):
            element = list(element.items())
            return cnt + calculate_structure_sum(element) + calculate_structure_sum(structure[1:])

    elif isinstance(structure, str):
        return cnt + len(structure) + calculate_structure_sum(structure[1:])
    elif isinstance(structure, int) or isinstance(structure, float):
        return cnt + structure
    elif isinstance(structure, set) or isinstance(structure, tuple):
        structure = list(structure)
        return cnt + calculate_structure_sum(structure)
    elif isinstance(structure, dict):
        structure = list(structure.items())
        return cnt + calculate_structure_sum(structure)
    elif structure == []:
        return 0


data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)


