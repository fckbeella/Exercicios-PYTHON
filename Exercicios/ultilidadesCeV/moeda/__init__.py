def aumentar(a,b,format=False):
    b = b/100
    if format == False:
        return a*b+a
    else:
        return monetario(a*b+a)

def diminuir(a,b,format=False):
    b = b/100
    c = a*b
    if format == False:
        return a-c
    else:
        return monetario(a-c)

def metade(p,format=False):
    if format == False:
        return p/2
    else:
        return monetario(p/2)

def dobro(p,format=False):
    if format == False:
        return p+p
    else:
        return monetario(p+p)

def monetario(p):
    return f'R${p:.2f}'.replace('.',',')

def resumo(a=0,b=0,c=0):
    print('=' * 30)
    print(f'RESUMO DO VALOR'.center(30))
    print('=' * 30)
    print(f'Preço analisado: \t{monetario(a)}')
    print(f'Dobro do preço: \t{dobro(a,format=True)}')
    print(f'Metade do preço: \t{metade(a,format=True)}')
    print(f'{b}% de aumento: \t{aumentar(a,b,format=True)}')
    print(f'{c}% de reduçao: \t{diminuir(a,c,format=True)}')
    print('=' * 30)