n = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Compasso', 9.99, 'Mochila', 120.32, 'Caneta', 1.50, 'Livro', 34.94)
print('-'*35)
print('{: ^35}'.format('PREÇO PRODUTOS'))
print('-'*35)
for pos in range(0,len(n)):
    if pos % 2 == 0:
        print(f'{n[pos]:.<30}', end='')
    else:
        print(f'R${n[pos]:<10.2f}')
print('-'*35)