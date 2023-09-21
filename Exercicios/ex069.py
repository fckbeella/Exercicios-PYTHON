ct = id = cont = cont2 = cont3 = 0
sexo = ' '
while True:
    try:
        id = int(input('Digite a idade: '))
        sexo = ' '
    except ValueError:
        print('\033[1,31mOps! Algo esta errado\033[m')
        continue
    else:
        while sexo not in 'MF':
            sexo = str(input('Digite o sexo: ')).strip().upper()[0]
        if id >= 18:
            cont2 += 1
        if sexo == 'M':
            cont3 += 1
        if sexo == 'F' and id <= 20:
            cont += 1
        ct = ' '
        while ct not in 'SN':
            ct = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]

        if ct == 'N':
            break
print(f'O total de pessoa com mais de 18 anos é: {cont2}')
print(f'O total de pessoa do sexo masculino é: {cont3}')
print(f'O total de mulheres com menos de 20 anos é: {cont}')