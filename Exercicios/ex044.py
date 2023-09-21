p = float(input('Digite o valor do produto: R$'))
vd = p-p*0.10
vc = p-p*0.05
c3 = p*0.20+p
print('Qual a forma de pagamento: \033[1;34m\n1 - A vista no dinheiro \n2 - A vista no cartão \n3 - 2x no cartão \n4 - 3x no cartão\033[m')
e = int(input('Escolha: '))
if e == 1:
    print(f'Você recebeu 10% de desconto, valor a ser pago: \033[1;32mR${vd:.2f}\033[m')
elif e == 2:
    print(f'Você recebeu 5% de desconto, valor a ser pago: \033[1;32mR${vc:.2f}\033[m')
elif e == 3:
    print(f'O valor a ser pago é: \033[1;32mR${p}\033[m parcelado de 2x \033[1;32mR${p/2:.2f}\033[m')
elif e == 4:
    print(f'O valor a ser pago é: \033[1;32mR${c3}\033[m parcelado de 3x \033[1;32mR${c3/3:.2f}\033[m')
else:
    print('\033[1;31mOpção de pagamento não existe.')
