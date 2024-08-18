def print_params(a=1, b='string', c=True):
    print(a, b, c)


print_params(b = 25)
print_params(c = [1,2,3])

values_list = [11, 'Urban', False]
values_dict = {'a': 111, 'b': True, 'c': 'Python'}

print_params(*values_list)
print_params(**values_dict)

values_list2 = ['Moscow', 600]
print_params(*values_list2, 42)


values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)