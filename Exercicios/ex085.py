lis = []
for c in range(0,7):
    num = int(input('Digite um número: '))
    lis.append(num)
lis.sort()
print(f'Os valores par digitado foram: ', end='' )
for num in lis:
    if num % 2 == 0:
        print(f'{num}..', end='')
print(f'\nOs valores impar digitado foram: ',end='')
for num in lis:
    if num % 2 == 1:
        print(f'{num}..', end='')


'''num = [[],[]]
valor = 0
for c in range(0,7):
    valor = int(input('Digite um valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    if valor % 2 == 1:
        num[1].append(valor)
print(num)'''