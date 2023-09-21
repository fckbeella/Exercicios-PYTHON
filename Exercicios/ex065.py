n = 0
l = []
p1 = 'S'
cont = 0
s = 0
total = 0
while p1 in 'Ss':
    n = int(input('Digite um número: '))
    p1 = input('Quer continuar ? [S/N]').strip().upper()
    cont += 1
    s = s + n
    total = cont
    l.append(n)
print(f'O menor número é: \033[1;32m{l[0]}\033[m o maior número: \033[1;32m{l[-1]}\033[m')
print(f'A média entre os valores foi: \033[1;32m{s/total}\033[m')
