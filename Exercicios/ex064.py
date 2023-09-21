n = 0
s = 0
cont = 0
while n != 999:
    n = int(input('Digite um número: '))
    cont += 1
    s = s + n
print(f'A quantidade de números digitados foi: {cont-1}')
print(f'A soma dos números digitados é: {s-999}')

