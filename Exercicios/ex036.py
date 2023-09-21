cs = float(input('Qual o valor da casa? R$'))
sl = float(input('Qual o valor do seu salário? R$'))
a = float(input('Deseja terminar o pagamento em quantos anos? '))
m = a*12
if cs/m <= sl*0.3:
    print('Empréstimo \033[1;32mAPROVADO\033[m.')
    print(f'A sua prestação será: R${cs/m:.2f} por {m:.0f} meses ou {a:.0f} anos.')
else:
    print('Empréstimo \033[1;31mNEGADO\033[m.')
