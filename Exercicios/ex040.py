a1 = float(input('Nota prova 1: '))
a2 = float(input('Nota prova 2: '))
m = (a1+a2)/2
if m<5.0:
    print(f'Sua media foi de: {m}')
    print('\033[4;31mREPROVADO\033[m')
elif m>=7.0:
    print(f'Sua media foi de: {m}')
    print('\033[4;32mAPROVADO\033[m')
elif 6.9 > m >= 5:
    print(f'Sua media foi de: {m}')
    print('\033[4;33mRECUPERAÇÃO\033[m')
