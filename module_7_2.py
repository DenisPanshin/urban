def custom_write(file_name, strings):
    my_dict = {}
    num = 1
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in strings:
            my_dict.update({(num, file.tell()): i})
            num += 1
            file.write(i + '\n')

    return my_dict


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
