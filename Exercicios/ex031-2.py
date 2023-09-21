n = float(input('Qual a distância da viagem? '))
n1 = n*0.50
n2 = n*0.45
if n<=200:
    print(f'A sua viagem irá custar: R${n1}')
else:
    print(f'A sua viagem irá custar: R${n2}')