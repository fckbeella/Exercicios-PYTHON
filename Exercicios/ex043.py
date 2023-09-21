n = input('Qual seu nome: ')
a = float(input('Qual a sua altura: '))
p = float(input('Qual o seu peso: '))
imc = p/a**2
if imc <18.5:
    print(f'Olá \033[1;35m{n}\033[m, seu imc é de \033[1;35m{imc:.2f}\033[m e você está \033[1;31mAbaixo do peso\033[m.')
elif imc >= 18.5 and imc < 25:
    print(f'Olá \033[1;35m{n}\033[m, seu imc é de \033[1;35m{imc:.2f}\033[m e você está no \033[1;31mPeso ideal\033[m.')
elif imc > 25 and imc < 30:
    print(f'Olá \033[1;35m{n}\033[m, seu imc é de \033[1;35m{imc:.2f}\033[m e você está com \033[1;31mSobrepeso\033[m.')
elif imc > 30 and imc < 40:
    print(f'Olá \033[1;35m{n}\033[m, seu imc é de \033[1;35m{imc:.2f}\033[m e você está com \033[1;31mObesidade\033[m.')
elif imc > 40:
    print(f'Olá \033[1;35m{n}\033[m, seu imc é de \033[1;35m{imc:.2f}\033[m e você está com \033[1;31mObesidade mórbida\033[m.')