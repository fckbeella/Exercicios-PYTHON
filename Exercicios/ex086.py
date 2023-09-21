mtx = [[0, 0, 0],
       [0, 0, 0],
       [0, 0, 0]]
for l in range(0,3):   # Este é o início do primeiro loop externo que percorre as linhas da matriz. A variável l representa o índice da linha atual e varia de 0 a 2 (pois há 3 linhas).
    for c in range(0,3):   # Aqui temos um loop interno que percorre as colunas da matriz. A variável c representa o índice da coluna atual e também varia de 0 a 2 (pois há 3 colunas).
        mtx[l][c] = int(input(f'Digite um valor [{l},{c}]: '))   #O valor é atribuído à posição mtx[l][c], ou seja, à linha l e à coluna c da matriz.
for l in range(0,3):
    for c in range(0,3):
        print(f'[{mtx[l][c]}]', end='')
    print()
