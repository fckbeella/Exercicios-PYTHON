import random
input('\033[1;34mVamos jogar impar ou par!!\033[m')
cont = 0
s = 0
while True:
    n = int(input('Escolha um número: '))
    es = input('Esse numero é Impar ou par [I/P]? ').strip().upper()[0]
    com = random.randint(1,10)
    s = n + com
    if es == 'I' and s%2 == 1:
        print('\033[1;32mPARABENS! Você ganhou\033[m')
        print(f'Jogador \033[1;31m{n}\033[m + Computador \033[1;31m{com}\033[m = \033[1;36m{s}\033[m')
        cont += 1
    elif es == 'P' and s%2 == 0:
        print('\033[1;32mPARABENS! Você ganhou\033[m')
        print(f'Jogador \033[1;31m{n}\033[m + Computador \033[1;31m{com}\033[m = \033[1;36m{s}\033[m')
        cont += 1
    elif es != 'IP':
        print('\033[1;31mVocê digitou algo errado, tente novamente.\033[m')
    else:
        break
print(f'GAME OVER! Você venceu \033[1;35m{cont}\033[m vezes.')
