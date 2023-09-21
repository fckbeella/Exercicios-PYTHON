a = input('Digite o comprimento da maior reta: ')
b = input('Digite o comprimento da segunda reta: ')
c = input('Digite o comprimento da terceira reta: ')
if a <= b+c and b <= a+c and c <= a+b:
    print('Com esses valores é possível fazer um triangulo.')
else:
    print('Com esses valores não é possível fazer um triangulo.')