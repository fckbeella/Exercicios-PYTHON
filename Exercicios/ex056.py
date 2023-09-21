mih = 0
nv = ''
i1 = 0
i2 = i1
s1 = 0
for c in range(1,5):
    n = input(f'Digite o nome da pessoa {c}: ')
    i = int(input(f'Digite a idade da pessoa {c}: '))
    print(f'Digite o sexo da pessoa {c}:\n1 - Feminino \n2 - Masculino ')
    s = int(input('Escolha: '))
    i1 = i1+i
    i2 = i1/4
    if c == 1 and s == 2:
        mih = i1
        nv = n
    if s == 2 and i > mih:
        mih = i
        nv = n
    if i < 20 and s == 1:
        s1 += 1
print(f'O homem mais velho é: \033[1;36m{nv}\033[m')
print(f'A media de idade entre as pessoas é de: \033[1;36m{i2}\033[m anos')
if s1 !=0:
    print(f'\033[1;36m{s1}\033[m Mulheres tem menos de 20 anos')
else:
    print('Não tem mulheres com menos de 20 anos')