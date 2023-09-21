M = ('M')
F = ('F')
n = 0
while n != M and n != F:
    n = input('Digite o seu sexo: [F/M]: ').upper()[0]
print('\033[1;32mSexo computado.\033[m')

