n = int(input('Tamanho da sequência de fibonacci: '))
ter1 = 1
ter2 = 1
cont = 3
print(f'{ter1} > {ter2}',end='')
while cont <= n:
    ter3 = ter1 + ter2
    print(f' > {ter3}',end='')
    ter1 = ter2
    ter2 = ter3
    cont+=1
print(' > FIM')