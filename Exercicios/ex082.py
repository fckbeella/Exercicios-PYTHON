p1 = 'Ss'
n = []
ni = []
np = []
while p1 in 'Ss':
    v = int(input('Digite um número: '))
    n.append(v)
    p1 = input('Quer continuar ? [S/N]').strip().upper()[0]
    if v % 2 == 1:
        ni.append(v)
    elif v % 2 == 0:
        np.append(v)
print(f' Os números digitados foi: {n}')
print(f' Os números impares digitados foi: {ni}')
print(f' Os números pares digitados foi: {np}')
