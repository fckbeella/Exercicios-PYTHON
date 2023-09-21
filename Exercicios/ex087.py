mtx = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
s = 0
sc = 0
mai = 0
for l in range(0,3):
    for c in range(0,3):
        mtx[l][c] = int(input(f'Digite um valor [{l},{c}]: '))
        s += mtx[l][c]
        sc += mtx[l][2]                                       #Dentro do loop externo, a variável sc é atualizada somando o valor da coluna de índice 2 (terceira coluna) na linha atual. Isso resultará na soma dos valores da terceira coluna.
print(f'A soma de todos os números da matriz é : {s}')
print(f'A soma dos números da 3º coluna é: {sc}')

mai = mtx[1][0]                                               #Aqui, a variável mai é inicializada com o primeiro valor da segunda linha
for c in range(0,3):                                          #Dentro do loop, verifica-se se o valor na segunda linha e na coluna atual é maior do que o valor atual de mai.
    if mtx[1][c] > mai:
        mai = mtx[1][c]
print(f'O maior valor da segunda linha é: {mai}')

for l in range(0,3):
    for c in range(0,3):
        print(f'[{mtx[l][c]:^5}]', end='')
    print()
