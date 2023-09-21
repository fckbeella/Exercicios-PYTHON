pa = []
pe = []
e = input('Digite uma expressão: ')
for c in e:
    pa = e.count('(')
    pe = e.count(')')
if pa == pe:
    print('Essa expressão é valida.')
else:
    print('Essa expressão está errada.')