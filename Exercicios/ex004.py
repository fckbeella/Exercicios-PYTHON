n = input('Digite algo: ')
print('O tipo primitivo desse valor é ', type(n))
print('É um numero? \033[1;31m{}\033[m'.format(n.isnumeric()))
print('É alfabético? \033[1;32m{}\033[m'.format(n.isalpha()))
print('É alfanumérico? \033[1;33m{}\033[m'.format(n.isalnum()))
print('Está capitalizada? \033[1;34m{}\033[m'.format(n.istitle()))



