t = int(input('Qual o número do termo: '))
r = int(input('Qual o número da razão: '))
d = t + (11 - 1)*r
for c in range(t,d,r):
     print(c, end=' > ')
print('ACABOU')
