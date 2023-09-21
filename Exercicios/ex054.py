from datetime import date
s = 0
s1 = 0
for c in range(1,8):
    a = int(input('Digite ano de nascimento: '))
    a1 = date.today().year - a
    if a1 >= 18:
       s += 1
    else:
       s1 += 1
print(f'{s} pessoas atingiram a maioridade')
print(f'{s1} pessoas nao atingiram a maioridade')