n = int(input('Digite um numéro: '))
b = bin(n)
o = oct(n)
h = hex(n)
print('Qual será a base de conversão: \n1 = binario \n2 = octal \n3 = hexadecimal')
n1 = int(input('Escolha: '))
if n1 == 1:
    print(f'O numéro em binario é: \033[1;31m{b}\033[m')
elif n1 == 2:
    print(f'O numéro em octal é: \033[1;31m{o}\033[m')
elif n1 == 3:
    print(f'O numéro em hexadecimal é: \033[1;31m{h}\033[m')
else:
    print('Opção não existe, tente novamente')
