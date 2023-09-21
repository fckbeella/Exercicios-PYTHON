from datetime import datetime
dados = {}
dados['Nome'] = input('Digite o nome da pessoa: ')
dados['Ano Nascimento'] = int(input('Digite o ano de nascimento: '))
dados['Idade'] = datetime.now().year - dados["Ano Nascimento"]
dados['CTPS'] = int(input('Digite o numero da CTPS (0 se nao tiver): '))

if dados["CTPS"] != 0:
    dados['AnoC'] = int(input('Digite o ano da 1º contrataçao: '))
    dados['Salario'] = float(input('Digite o salario: '))
    dados['Contribuiçao'] = datetime.now().year - dados["AnoC"]

    if dados["Contribuiçao"] < 65:
        for k, v in dados.items():
            print(f'{k} - {v}')
        print(f'Voce contribuiu por {dados["Contribuiçao"]} anos.')
        print(f'Vai se aposentar daqui {65 - dados["Contribuiçao"]} com {dados["Idade"] + (65 - dados["Contribuiçao"])} anos')
    else:
        for k, v in dados.items():
            print(f'{k} - {v}')
        print('Voce ja fez a contribuiçao necessaria para aposentar.')
else:
    print('Voce ainda nao possui carteira de trabalho')

