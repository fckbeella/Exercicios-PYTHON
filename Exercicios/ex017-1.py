import math
o = float(input('Qual o valor do cateto oposto: '))
a = float(input('Qual o valor do cateto adjacente: '))
print(f'O valor do comprimento da hipotenusa é: {math.sqrt((o*o)+(a*a)):.2f}')
print(f'O valor do comprimento da hipotenusa é: {math.sqrt(o*o+a*a):.2f}')
print(f'O valor do comprimento da hipotenusa é: {(o*o+a*a)**(1/2):.2f}')
print(f'O valor do comprimento da hipotenusa é: {math.hypot(o,a):.2f}')