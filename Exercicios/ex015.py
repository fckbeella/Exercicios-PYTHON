input('Vamos saber o valor do seu aluguel.\nLembrando que é cobrado R$60 por dia e R$0,15 por km rodado.')
km = float(input('Quantos quilômetros rodados? '))
d = float(input('Quantos dias você ficou com o carro? '))
print(f'O valor total de seu aluguel é: R${(km*0.15)+(d*60)}')