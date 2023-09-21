n = (int(input('Digite 1ª número: ')),
    int(input('Digite 2ª número: ')),
    int(input('Digite 3ª número: ')),
    int(input('Digite 4ª número: ')))
cont = 0
print(f'Você digitou os valores: {n}')
print(f'O valor 9 apareceu {n.count(9)} vezes.')
if 3 in n:
    print(f'O valor 3 apareceu na {n.index(3)+1}ª posição.')
else:
    print('O valor 3 não foi digitado.')
for c in range(0,4):
    if n[c] % 2 == 0:
        cont += 1
print(f'Os valores pares digitados foram {cont} vezes.')