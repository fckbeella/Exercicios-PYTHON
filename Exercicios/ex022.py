n = str(input('Digite seu nome completo: '))
h = n.split()
p = ''.join(h)
print(n.upper())
print(n.lower())
print(''.join(h))
print(f'O número total de letras é: {(len(p))}')
print(h[0])
print(f'O numero de letras no primeiro nome é: {(len(h[0]))}')

