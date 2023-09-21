n = int(input('Digite um numéro inteiro: '))
n1 = int(input('Digite outro numéro inteiro: '))
if n > n1:
    print(f'O \033[1;34mPRIMEIRO\033[m numéro é maior.')
elif n < n1:
    print(f'O \033[1;34mSEGUNDO\033[m numéro é maior.')
else:
    print(f'\033[1;31mOs dois valores são iguais.')