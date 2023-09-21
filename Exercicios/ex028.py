import random
print('\033[1;34mAdivinhe o numero que estou pensando de 0 á 5.\033[m')
while input:
    n = int(input('Digite o numero: '))
    n1 = random.randint(0,5)
    if n == n1:
        print('\033[1;32mPARABENS! Você acertou.\033[m')
    else:
        print(f'\033[1;31mSinto muito. Mas o número pensado foi\033[m \033[4;33m{n1}\033[m.')

    continuar = input('Deseja tentar de novo?(S/N): ')
    if continuar.upper()!='S':
        break
print('Volte depois para brincarmos mais.')
