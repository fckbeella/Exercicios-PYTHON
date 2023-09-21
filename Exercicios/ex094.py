dados = dict()
dados00 = []
mul = []
acima_pessoas = []
cont = tot = 0
while True:
    dados['Nome'] = input('Digite o nome: ')
    while True:
        dados['Sexo'] = input('Digite o sexo: ').upper()[0]
        if dados['Sexo'] in 'MF':
            break
        print('Opps! Digite novamente [M/F]')
    dados['Idade'] = int(input('Digite a idade: '))
    cont += 1
    dados00.append(dados.copy())
    tot += dados['Idade']
    while True:
        p1 = input('Quer continuar ? [S/N]').strip().upper()[0]
        if p1 in 'SN':
            break
        print('Opps! Digite novamente [S/N]')
    if p1 == 'N':
        break
    if dados['Sexo'] == 'F':
        mul.append(dados['Nome'])
    if dados['Idade'] > tot/cont:
        acima_pessoas.append(dados['Nome'])
print(f'O Total de {cont} pessoas foram cadastradas')
print(f'A media de idade e: {tot/cont}')
print(f'Lista de mulheres: {mul}')
print(f'Lista de pessoas com idade acima da media: {acima_pessoas}')

