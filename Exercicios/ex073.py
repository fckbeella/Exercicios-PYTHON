br = ('Botafogo', 'Palmeiras', 'Grêmio', 'Flamengo', 'Fluminense', 'Bragantino',
      'Athletico-PR', 'Fortaleza', 'Atlético-MG', 'Cuiabá', 'São paulo', 'Cruzeiro',
      'Corinthians', 'Internacional', 'Goás', 'Bahia', 'Santos', 'Vasco', 'Coritiba', 'América-MG')
print(f'Os 5 primeiros times: {br[0:5]}')
print(f'Os 4 últimos colocados: {br[-4:]}')
print(f'Os times em ordem alfabética fica: {sorted(br)}')
print(f'O Atlético-MG está na {br.index("Atlético-MG")+1}ª posição')