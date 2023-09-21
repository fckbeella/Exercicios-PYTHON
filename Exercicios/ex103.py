def ficha(n='', g=0):
    if n == '':
        print(f'O jogador desconhecido, fez {g} gol(s) no campeonato.')
    else:
        print(f'O jogador {n}, fez {g} gol(s) no campeonato.')


nome = input('Digite o nome do jogador: ')
gols = input('Quantos gols esse jogador fez: ')
if gols == '':
    gols = 0
ficha(n=nome, g=gols)