numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:
    if i == 1:
        continue
    flag = False
    for j in range(2, i):
        if i % j == 0:
            flag = True
            break
    if flag:
        not_primes.append(i)
    else:
        primes.append(i)
print(primes)
print(not_primes)



