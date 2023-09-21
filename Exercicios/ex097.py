def escreva(msg):
    print('-=' * (len(msg)))
    print(f'{msg:^{len(msg)*2}}')
    print('-=' * (len(msg)))

texto = str(input('Digite uma frase: '))
escreva(texto)
