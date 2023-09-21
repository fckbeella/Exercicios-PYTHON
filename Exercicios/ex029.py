n = float(input('Qual a velocidade do carro: '))
n1 = (n-80)*7
if n>80:
    print(f'Você esta acima do limite de velocidade. Recebeu uma multa no valor de: R${n1:.2f}')
