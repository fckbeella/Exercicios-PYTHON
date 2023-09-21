n = []
for c in range(1,6):
    n.append(input(f'Digite o {c}º número: '))
print(f'O menor valor é: \033[1;32m{min(n)}\033[m e está na posição ',end='')
for i, v in enumerate(n):
    if v == min(n):
        print(f'\033[1;31m{i}\033[m..', end='')
print(f'\nO maior valor é: \033[1;32m{max(n)}\033[m e está na posição ',end='')
for i, v in enumerate(n):
    if v == max(n):
        print(f'\033[1;31m{i}\033[m..', end='')