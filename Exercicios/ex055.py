ll = []
l = []
for c in range(1,6):
    p = input(f'Digite o peso da peso nº{c}: ').split()
    ll += p
    l = sorted(ll, key=int)
print(f'O maior peso é: {(l[4])}')
print(f'O menor peso é: {(l[0])}')
