p1 = 'Ss'
n = []
while p1 in 'Ss':
    n.append(int(input('Digite um valor: ')))
    n.sort(reverse=True)
    p1 = input('Quer continuar ? [S/N]').strip().upper()[0]

print(f'A quantidade de números digitados é: {len(n)}')
print(f'Ordem decrescente números digitados: {n}')
if 5 in n:
    print('O número 5 está na lista')
else:
    print('O número 5 não foi digitado')
