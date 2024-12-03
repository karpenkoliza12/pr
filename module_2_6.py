import random
n = random.randint(3, 20)
print(n)

pas = ''
for i in range(1, n):
    for j in range(i + 1, n):
        if n % (i+j) == 0:
            pas += str(i) + str(j)
print(pas)

