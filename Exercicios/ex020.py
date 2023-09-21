import random
print('Digite o nome dos alunos a seguir:')
a = input('')
b = input('')
c = input('')
d = input('')
r1 = random.sample([a,b,c,d],k=4)
print(f'A sequencia escolhida foi: {r1}')