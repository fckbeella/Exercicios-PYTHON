import random
dic = {}
rank = []
print('Chame seus amigos e vamos ver quem tema sorte grande.')
for c in range(0,4):
    dic['Num'] = random.randint(1, 6)
    rank.append(dic.copy())
    print(f'Jogador {c+1}º - Tirou {dic["Num"]} no dado.')
    rank.sort(key=lambda x:x["Num"], reverse=True)
print()
print('Resultado sorteio')
for pos, rank in enumerate(rank, start=1):
    print(f'{pos}º Lugar: {rank["Num"]}')

