s = cont = cont2 = menor = 0
barato = ''
while True:
    nm = str(input('Digite o nome do produto: ')).strip()
    pc = float(input('Digite o valor do produto: R$'))
    ct = input('Deseja colocar mais produtos?[S/N]: ').strip().upper()[0]
    cont2 += 1
    s = s + pc
    if ct == 'N':
        break
    if cont2 == 1 or pc < menor:
        menor = pc
        barato = nm
    if pc >= 1000:
        cont+= 1
print(f'O total da compra é: R${s}')
print(f'{cont} produto custaram mais de R$1000')
print(f'O produto mais barato é {barato} custando R${menor}')