import math
o = float(input('Qual o valor do cateto oposto: '))
a = float(input('Qual o valor do cateto adjacente: '))
o1 = o*o
a1 = a*a
print(f'O valor do comprimento da hipotenusa é: {math.sqrt(o1+a1):.2f}')