from datetime import date
a = int(input('Ano de nascimento: '))
i = date.today().year-a
if i <= 9:
    print(f'Sua idade é: {i}')
    print('Categoria: Mirim')
elif i <= 14:
    print(f'Sua idade é: {i}')
    print('Categoria: Infantil')
elif i <= 19:
    print(f'Sua idade é: {i}')
    print('Categoria: júnior')
elif i <= 25:
    print(f'Sua idade é: {i}')
    print('Categoria: Sênior')
else:
    print(f'Sua idade é: {i}')
    print('Categoria: Master')