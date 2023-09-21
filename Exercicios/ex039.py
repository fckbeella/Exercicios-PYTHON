d = int(input('Digite o ano de seu nascimento: '))
d1 = 2023-d
if d1 < 18:
    print(f'Sua idade é de {d1} anos, falta \033[1;31m{18-d1}\033[m ano para seu alistamento.')
elif d1 == 18:
    print(f"Sua idade é de {d1} anos, você deve se alistar \033[4;31mIMEDIATAMENTE\033[m.")
elif d1 > 18:
    print(f'OPS! Já passou \033[1;31m{d1-18}\033[m ano da data de alistamento.')
print('Acesse o site do exército para mais informações.')