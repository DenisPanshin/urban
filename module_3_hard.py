count = 0
def calculate_structure_sum(lst):
    for el in lst:
        if isinstance(el, (list, tuple, dict, set)):
            calculate_structure_sum(el)
        else:
            if isinstance(lst, dict):
                global count
                count += lst[el]
                count += len(el)
            elif isinstance(el, str):
                count += len(el)
            else:
                count += el
    return count
lst = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])]

print(calculate_structure_sum(lst))
