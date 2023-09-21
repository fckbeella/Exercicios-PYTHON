n = int(input('Digite o ano desejado: '))
if n%4 == 0 and n%100 !=0 or n%400 == 0:
    print(f'O ano de {n} é bissexto')
else:
    print(f'O ano de {n} não é bissexto')