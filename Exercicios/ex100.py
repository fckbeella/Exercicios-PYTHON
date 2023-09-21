import random
def sorteia():
    num = []
    for c in range(0,5):
        num.append(random.randint(1,100))
    print(f'Numeros sorteados: {num}')
    return num
def soma_par(num):
    s = 0
    for n in num:
        if n % 2 == 0:
            s += n
    return s

ns = sorteia()
sp = soma_par(ns)
print(f'A soma dos numeros pares sorteados e: {sp}')