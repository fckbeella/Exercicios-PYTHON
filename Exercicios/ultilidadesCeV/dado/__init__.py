def leiadinheiro(p):
    while True:
        n = input(p).replace(',','.')
        n1 = n.replace('.','1')
        if n1.isnumeric():
            return float(n)
        else:
            print(f'\033[1;31mERRO:\033[m \033[1;33m{n}\033[m \033[1;31mnão é um valor valido.\033[m')

def leiaint(p):
    while True:
        try:
            n = int(input(p))
        except:
            print('\033[1;31mERRO: não é um numero inteiro.\033[m')
        else:
            return n

def leiafloat(p):
    while True:
        try:
            n = float(input(p))
        except:
            print('\033[1;31mERRO: não é um numero real.\033[m')
        else:
            return n