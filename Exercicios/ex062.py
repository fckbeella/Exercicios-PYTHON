ter = int(input('Qual o número do termo: '))
raz = int(input('Qual o número da razão: '))
cont = 1
mais = 10
total = 0
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{ter} > ', end='')
        ter += raz
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos a mais você quer ver: '))
print('Programa finalizado.')
