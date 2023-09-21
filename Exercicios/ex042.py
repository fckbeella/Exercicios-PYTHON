a = float(input('Digite o comprimento da primeira reta: '))
b = float(input('Digite o comprimento da segunda reta: '))
c = float(input('Digite o comprimento da terceira reta: '))
if a <= b+c and b <= a+c and c <= a+b:
    print('\033[1;32mCom esses valores é possível fazer um triangulo.\033[m')
    if a == b == c:
        print('Com esses valores forma um \033[7mTriangulo equilátero\033[m')
    elif b == c != a:
        print('Com esses valores forma um \033[7mTriangulo isósceles\033[m')
    else:
        print('Com esses valores forma um \033[7mTriangulo escaleno\033[m')
else:
    print('\033[4;31mCom esses valores não é possível fazer um triangulo.\033[m')