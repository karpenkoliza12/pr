numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:
    is_primes = True
    for j in range(2, i-1):

        if i % j == 0:
            is_primes = False
            break
    if i != 1:
        if is_primes:
            primes.append(i)
        else:
            not_primes.append(i)

print(primes)
print(not_primes)