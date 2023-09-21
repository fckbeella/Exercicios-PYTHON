n = str(input('Digite seu nome completo: ').lower().title()).split()
print(f'Ficando assim: \033[7m{(n[0])} {(n[-1])}\033[m')
