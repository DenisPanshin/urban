def is_prime(func):
    def wrapper(*args):
        res = func(*args)
        delitel = 0
        for i in range(1, res + 1):
            if res % i == 0:
                delitel += 1
        if delitel == 2:
            print('Простое')
            return res
        else:
            print('Составное')
            return res

    return wrapper


@is_prime
def sum_three(*args):
    res = 0
    for i in args:
        res += i
    return res


result = sum_three(2, 3, 6)
print(result)
