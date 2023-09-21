def contador():
    print('-=' * 20)
    print('O contador de 1 ate 10, de 1 em 1: ')
    for c in range(1,11,1):
        print(c, end=' ')

def contador2():
    print('-=' * 20)
    print('O contador de 10 ate 0, de 2 em 2: ')
    for y in range(10,-1,-2):
        print(y, end=' ')

def contador3(a,b,c):
    print('-=' * 20)
    print('O contador personalizado: ')
    if a > b:
        for i in range(a,b,-c):
            print(i, end=' ')
    else:
        for i in range(a,b,c):
            print(i, end=' ')
    print()
    print('-=' * 20)


contador()
print()
contador2()
print()
print()
print('Digite o inicio, fim, passo para um contador personalizado: ')
a = int(input('Inicio: '))
b = int(input('Fim: '))
c = int(input('Passo: '))
contador3(a,b,c)