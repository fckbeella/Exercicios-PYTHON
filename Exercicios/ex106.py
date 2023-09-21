from time import sleep
while True:
    com = str(input('\033[1;31mDigite a funçao ou Biblioteca ("FIM" para sair): '))
    print('\033[7;36;40m=' * 48)
    print(f'{"ANALISANDO":^48}')
    print('\033[7;36;40m=' * 48)
    print('\033[m')
    sleep(1)
    if com.upper() == 'FIM':
        break
    else:
        print('\033[7m', end='')
        help(com)
        print('\033[m')