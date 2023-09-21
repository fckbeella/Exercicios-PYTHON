numero_1 = 0
numero_2 = 0
while True:
    numero_1 = int(input('Digite um número: '))
    numero_2 = int(input('Digite um número: '))
    opc = int(input('Digite uma opção: \n\033[1;31m1\033[m - Somar \n\033[1;31m2\033[m - Multiplicar \n\033[1;31m3\033[m - Maior \n\033[1;31m4\033[m - Números novos \n\033[1;31m5\033[m - Sair do programa \n\033[1;36mEscolha:\033[m '))
    l = [numero_1, numero_2]
    mar = sorted(l, key=int)
    if opc == 1:
        print(f'A soma dos números é: \033[1;32m{numero_1+numero_2}\033[m')
        break
    elif opc == 2:
        print(f'A multiplicação dos números é: \033[1;32m{numero_1*numero_2}\033[m')
        break
    elif opc == 3:
        print(f'O maior número entre eles é: \033[1;32m{(mar[1])}\033[m')
        break
    elif opc == 4:
        continue
    elif opc == 5:
        break
    else:
        print('\033[1;31mOpção invalida.\033[m')
