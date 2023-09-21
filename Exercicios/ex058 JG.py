import random
n1 = random.randint(0,10)
print('\033[1;34mAdivinhe o numero que estou pensando de 0 á 10.\033[m')
a = False
n = 0
p = 0
while not a:
    n = int(input('Digite o numero: '))
    if n != n1:
        p += 1
        print(f'\033[1;31mSinto muito. Tente novamente.\033[m')
        if n > n1:
            print('\033[1;33mMenos...\033[mChute um numero menor.')
        elif n < n1:
            print('\033[1;33mMais...\033[mChute um numero maior.')
    elif n == n1:
        a = True
        print('\033[1;32mPARABENS! Você acertou.\033[m')
        print(f'O numero de tentativas foi: {p}')
        break
