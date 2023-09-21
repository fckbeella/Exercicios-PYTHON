def leiaint(v):
    while True:
        n = input(num)
        if n.isdigit():
            return n
        else:
            print('Digite um valor numerico.')


num = leiaint('Digite um numero: ')
print(f'O valor digitado foi {num}.')

