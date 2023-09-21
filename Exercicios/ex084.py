p1 = 'Ss'
dados0 = []
lis = []
mai = men = 0
while p1 in 'Ss':
    dados0.append(str(input('Nome: ')))
    dados0.append(int(input('Peso: ')))
    if len(lis) == 0:                           # Verifica se a lista lis está vazia
        mai = men = dados0[1]                   # Se estiver vazia, define mai e men como uma lista contendo o primeiro peso
    else:
        if dados0[1] > mai:                     # Compara o peso atual com o valor de mai (maior peso)
            mai = dados0[1]                     # Atualiza mai se o peso atual for maior
        if dados0[1] < men:                     # Compara o peso atual com o valor de men (menor peso)
            men = dados0[1]                     # Atualiza men se o peso atual for menor
    lis.append(dados0[:])                       # Adiciona uma cópia dos dados0 à lista lis
    dados0.clear()                              # Limpa os dados da lista dados0 para a próxima iteração
    p1 = input('Quer continuar ? [S/N]').strip().upper()[0]
print(f'Foram {len(lis)} pessoas cadastradas.')
print(f'O maior peso foi: {mai}Kg. De ', end='')
for p in lis:                                   # Percorre a lista lis para encontrar as pessoas com o maior peso
    if p[1] == mai:
        print(f'{p[0]}..',end='')               # Exibe os nomes das pessoas com o maior peso
print(f'\nO menor peso foi: {men}Kg. De ', end='')
for p in lis:                                   # Percorre a lista lis para encontrar as pessoas com o menor peso
    if p[1] == men:
        print(f'{p[0]}..', end='')              # Exibe os nomes das pessoas com o menor peso



