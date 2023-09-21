f = input('Digite uma frase: ').lower().split()
ff = ''.join(f)
if ff == ff[::-1]:
    print(f'\033[1;32m{ff}\033[m ao contrario \033[1;32m{ff[::-1]}\033[m ')
    print('Essa frase é um PALÍNDROMO')
else:
    print(f'\033[1;31m{ff}\033[m ao contrario \033[1;31m{ff[::-1]}\033[m ')
    print('Essa frase não é um PALÍNDROMO')