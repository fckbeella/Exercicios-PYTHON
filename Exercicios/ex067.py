cont = 0
while True:
    n = int(input('Digite um número: '))
    if n > 0:
        for cont in range(1,11):
            print(f'{n}x{cont} = {n * cont}')
            cont += 1
    else:
        break