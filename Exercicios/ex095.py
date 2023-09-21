jogadores = []

while True:
    jogador = {}

    jogador['nome'] = input('Nome do jogador: ')
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

    gols = []
    for partida in range(partidas):
        gols.append(int(input(f'Gols na partida {partida + 1}: ')))

    jogador['gols'] = gols
    jogador['total'] = sum(gols)

    jogadores.append(jogador)

    continuar = input('Deseja cadastrar outro jogador? (S/N): ').strip().upper()
    if continuar != 'S':
        break

print('-=' * 20)
print('Aproveitamento dos jogadores:')
for jogador in jogadores:
    print('-' * 30)
    print(f'Nome: {jogador["nome"]}')
    print(f'Quantidade de partidas: {len(jogador["gols"])}')
    print(f'Gols por partida: {", ".join(map(str, jogador["gols"]))}')
    print(f'Total de gols: {jogador["total"]}')