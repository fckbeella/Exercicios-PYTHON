t = int(input('Qual o número do termo: '))
r = int(input('Qual o número da razão: '))
cont = 1
ter = t
while cont <= 10:
    print(f'{ter}', end='')
    print(' > ' if cont < 10 else ' FIM', end='')
    ter += r
    cont += 1

