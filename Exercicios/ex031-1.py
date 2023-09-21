n = float(input('Qual a distância da viagem? '))
if n <= 200:
    p = n*0.50
else:
    p = n*0.45
print(f'A sua viagem irá custar: R${p}')