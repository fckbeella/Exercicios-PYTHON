def maior(*num):
    num = []
    cont = 0
    while True:
        num.append(int(input('Digite um valor: ')))
        p1 = input('Adicionar mais valores? [S/N]').strip().upper()[0]
        cont += 1
        if p1 in 'N':
            break
    print('-=' * 20)
    print(f'Os valores digitado: {num}, e o quantidade de numeros digitados e: {cont}')
    print(f'O maior valor e: {max(num)}')
    print('-=' * 20)

maior()