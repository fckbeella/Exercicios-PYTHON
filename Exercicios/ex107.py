from ultilidadesCeV import moeda

p = float(input('Digite um preço: R$'))
print(f'A metade de R${p} e {moeda.metade(p, format=True)}.')
print(f'O dobro de R${p} e {moeda.dobro(p,format=False)}.')
print(f'Aumentando 10%, temos {moeda.aumentar(p,10,format=True)}.')
print(f'Reduzindo 13%, temos {moeda.diminuir(p,13, format=True)}.')