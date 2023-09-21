p1 = 'Ss'
n = []
while p1 in 'Ss':
    try:
        v = int(input('Digite um valor: '))
        if v not in n:
            n.append(v)
            print('\033[1;32mValor computado\033[m')
        else:
            print('\033[1;33mValor duplicado! Digite outro valor...\033[m')
    except ValueError:
        print('\033[1;31mOps! Algo foi digitado errado...\033[m')
    finally:
        p1 = input('Quer continuar ? [S/N]').strip().upper()[0]
print(f'Os valores digitados: {sorted(n)}')