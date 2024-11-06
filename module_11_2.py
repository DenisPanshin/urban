from inspect import getmodule


def introspection_info(obj):
    type_ = type(obj)
    attr = [i for i in dir(obj) if i.startswith('__')]
    methods = [i for i in dir(obj) if not i.startswith('__')]
    module = getmodule(obj)
    my_dict = {'type': type_, 'attributes': attr, 'methods': methods, 'module': module}
    return my_dict


number_info = introspection_info('42')
print(number_info)
