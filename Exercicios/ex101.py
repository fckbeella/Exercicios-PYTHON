from datetime import date
def voto(a=0):
    idade = date.today().year - a
    if idade <= 15:
        print(f'Voce tem \033[1;36m{idade}\033[m anos, \033[1;32mNEGADO\033[m')
    elif idade > 16 and idade < 17:
        print(f'Voce tem \033[1;36m{idade}\033[m anos, \033[1;33mOPCIONAL\033[m')
    else:
        print(f'Voce tem \033[1;36m{idade}\033[m anos, \033[1;31mOBRIGATÓRIO\033[m')


ano = int(input('Digite o ano de seu nascimento: '))
voto(ano)
