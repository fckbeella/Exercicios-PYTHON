dados = {}
gols = []
dados['Nome'] = input('Nome jogador: ')
pt = int(input('Quantas partidas jogadas?  '))
for c in range(0,pt):
    gols.append(int(input(f'Gols na {c+1}º Partida: ')))
tot = sum(gols)
print(f'Nome jogador: {dados["Nome"]}')
for pos, gols in enumerate(gols, start=1):
    print(f'{pos}º Partida: {gols}')
print(f'O total de Gols foi: {tot}')