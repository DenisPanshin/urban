def apply_all_func(int_list, *functions):
    res = list(map(int, int_list))
    my_dict = {}
    for i in functions:
        my_dict.update({i.__name__: i(res)})
    return my_dict


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
