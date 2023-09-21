c = float(input('Qual a atual cotação do dolar: US$'))
e = float(input('Qual a atual cotação do euro: €'))
v = float(input('Qual o valor em reais você tem: R$'))
print(f'Com R${v} seu valor em dolar é: US${v/c:.2f} \nE em euro é: €{v/e:.2f}')
