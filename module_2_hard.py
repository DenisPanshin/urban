n = int(input(f'Введите число: '))
my_list = []
for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        # print(j)
        if n % (i + j) == 0:
            if f'{i}+{j}' in my_list:
                continue
            my_list.append(f'{i}{j}')

print(n, end=' - ')
print(*my_list, sep='')
