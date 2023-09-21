n = int(input('Primeiro número: '))
n1 = int(input('Segundo número: '))
n2 = int(input('Terceiro número: '))
l = [n,n1,n2]
n3 = sorted(l)
print(f'O maior número entre eles é: {(n3[2])}')
print(f'O menor numero entre eles é: {(n3[0])}')
