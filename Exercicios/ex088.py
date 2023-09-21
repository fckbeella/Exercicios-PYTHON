import random
npal = int(input('Digite número de palpites a serem gerados: '))
lis = []
num = []
for n in range(0,npal):
    for c in range(0,6):
        if num not in lis:
            num.append(random.randint(1,60))
        lis.append(num[:])
        num.clear()
        lis.sort()
    print(f'{n+1}º Palpite: {lis}')
    lis.clear()

