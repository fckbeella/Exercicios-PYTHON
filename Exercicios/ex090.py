lis = {}
lis['nome'] = str(input('Nome aluno: '))
lis['media'] = float(input('Media: '))
print(f'- Nome: {lis["nome"]}')
print(f'- Media: {lis["media"]}')
if lis["media"] > 7.0:
    print('- Passou')
elif lis["media"] <= 6.9 or lis["media"] >= 6:
    print('- Recuperaçao')
else:
    print('- Reprovado')

