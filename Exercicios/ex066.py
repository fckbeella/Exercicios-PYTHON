n = 0
s = 0
cont = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s = s + n
    cont += 1
print(f'A quantidade de números digitados foi: {cont}')
print(f'A soma dos números digitados é: {s}')
