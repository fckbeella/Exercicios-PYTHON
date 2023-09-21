l = []
for c in range(0,5):                               # O loop for irá iterar cinco vezes (0, 1, 2, 3, 4)
    n = int(input('Digite um valor: '))            # Solicita ao usuário para digitar um valor inteiro
    if c == 0 or n > l[-1]:                        # Verifica se é a primeira iteração ou se o valor inserido é maior que o último valor na lista
        l.append(n)                                # Adiciona o valor no final da lista "l"
    else:
        pos = 0                                    # Inicializa uma variável "pos" que será usada para percorrer a lista
        while pos < len(l):                        # Entra em um loop while que percorre a lista "l"
            if n <= l[pos]:                        # Verifica se o valor inserido é menor ou igual ao valor atual da posição da lista
                l.insert(pos,n)                    # Insere o valor na posição correta da lista, mantendo-a ordenada
                break
            pos += 1                               # Incrementa a variável "pos" para avançar na lista
print(l)


