import random
import emoji

print('\033[1;34mVamos jogar JOKENPÔ.\033[m')
while input:
    print('Considere: \n1 - Pedra, \n2 - Papel, \n3 - Tesoura')
    e = int(input('Escolha: '))
    p = random.randint(1,3)
    p1 = p
    if e == 1 and p1 == 3:
        print('\033[1;31mPEDRA X TESOURA\033[m')
        print('\033[1;32mPARABENS!Você ganhou.\033[m')
    elif e == 2 and p1 == 1:
        print('\033[1;31mPAPEL X PEDRA\033[m')
        print('\033[1;32mPARABENS!Você ganhou.\033[m')
    elif e == 3 and p1 == 2:
        print('\033[1;31mTESOURA X PAPEL\033[m')
        print('\033[1;32mPARABENS!Você ganhou.\033[m')
    elif e == 1 and p1 == 2:
        print('\033[1;31mPEDRA X PAPEL\033[m')
        print(f'\033[1;33mSinto muito, mas você perdeu\033[m')
    elif e == 2 and p1 == 3:
        print('\033[1;31mPAPEL X TESOURA\033[m')
        print(f'\033[1;33mSinto muito, mas você perdeu\033[m')
    elif e == 3 and p1 == 1:
        print('\033[1;31mTESOURA X PEDRA\033[m')
        print(f'\033[1;33mSinto muito, mas você perdeu\033[m')
    else:
        print('Temos um \033[1;36mEMPATE\033[m')

    continuar = input('Deseja tentar de novo?(S/N): ')
    if continuar.upper()!='S':
        break
print('Volte depois para brincarmos mais.')