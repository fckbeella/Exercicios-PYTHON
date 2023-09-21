import math
n = int(input('Digite um numero: '))
c = n
n1 = math.factorial(n)
while c > 0:
    print(f'\033[1;31m{c}\033[m', end='')
    print(' x ' if c > 1 else '=', end='')
    c -= 1
print(f'\033[1;32m {n1}\033[m')
