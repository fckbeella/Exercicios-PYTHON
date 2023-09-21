n = int(input('Digite um número: '))
t = 0
for c in range(1,n+1):
    if n % c == 0:
        t += 1
if t == 2:
    print(f'O número \033[1;32m{n}\033[m é primo.')
else:
    print(f'O número \033[1;31m{n}\033[m não é primo.')

