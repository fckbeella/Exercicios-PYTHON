lista = ('Cachorro', 'Peixe', 'Pudim', 'Belinha', 'Bolinha', 'Eixo')
for pos in lista:
    print(f'\nNa palavra \033[1;32m{pos}\033[m temos: ', end='')
    for letras in pos:
        if letras in 'AaEeIiOoUu':
            print(f'\033[1;31m{letras}\033[m', end='')