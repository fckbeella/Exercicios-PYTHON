s = 0                                       # Inicializa a variável "s" com 0 (será usada para calcular a soma dos valores)
c1 = 0                                      # Inicializa a variável "c1" com 0 (será usada para contar quantos valores se encaixam no critério)
for c in range(1,501,2):                    # Loop "for" que percorre números ímpares de 1 a 500
    if c % 3 == 0:                          # Verifica se o número "c" é divisível por 3 (seu resto é 0 quando dividido por 3)
        c1 = c1 + 1                         # Incrementa o contador "c1" para contar quantos números satisfazem o critério
        s = s+c                             # Adiciona o valor "c" à variável "s" para calcular a soma
print(f'A soma dos {c1} valores é: {s} ')


