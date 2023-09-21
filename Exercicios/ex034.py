n = float(input('Salario atual: R$'))
if n <= 1250:
   n1 = n+(n*0.15)
else:
   n1 = n+(n*0.10)
print(f'O aumento do salario foi para: \033[1;32mR${n1:.2f}')
